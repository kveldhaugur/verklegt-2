from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from main.models import ShoppingCart, Items, CartContains, PromoCodes
import json

# Create your views here.
def index(request):
    context = {}
    if request.session.session_key is not None:
        try:
            cart = ShoppingCart.objects.get(SessionID=request.session.session_key)
        except ShoppingCart.DoesNotExist:
            cart = None
        if cart is not None:
            cart_contains = cart.ItemsInCart.all()
            items = []
            total_price = 0
            for cart_item in cart_contains:
                item = cart_item.ItemID
                items.append((item, cart_item.Quantity))
                total_price += int(cart_item.Quantity) * item.Price
            context['items_in_cart'] = items
            context['total'] = total_price
            return render(request, 'cart/index.html', context)
    else:
        request.session.create()
    context['items_in_cart'] = None
    context['message'] = "Your cart contains no items, try adding some to the cart"
    return render(request, 'cart/index.html', context)


def activate_promo(request):
    data = json.loads(request.body)
    promo_name = data['promo_name']
    price = data['total_price']
    try:
        promo = PromoCodes.objects.get(Name=promo_name)
        total_after_promo = round(int(price) - int(price) * promo.Discount, 2)
    except PromoCodes.DoesNotExist:
        return JsonResponse({
            'error': 'Promo not found'
        }, safe=False)

    return JsonResponse(
        {
            'message': 'Promo accepted',
            'data': total_after_promo
        }, safe=False)


def update_item(request):
    data = json.loads(request.body)

    itemID = data['ItemID'] #21312
    action = data['action'] #add
    quantity = int(data['quantity']) #1

    product = Items.objects.get(ItemID=itemID)
    # check first if item is available
    if product.Quantity_available <= 0 and action == 'add':
        return JsonResponse({'error': 'Failed to update cart, no available in stock'}, safe=False)
    if request.session.session_key is None:
        request.session.create()
    customer = Session.objects.get(session_key=request.session.session_key)

    cart = get_or_create_cart(customer)
    # add item to cart
    cart_contains = get_or_create_cart_contains(product, cart, customer)
    if quantity > 1:
        if 0 < product.Quantity_available < quantity:
            return JsonResponse({'error': 'Failed to update, cannot add more products than are available'}, safe=False)
        cart_contains.Quantity = quantity
    elif quantity == 1 and action == 'add':
        if product.Quantity_available < (cart_contains.Quantity + 1):
            return JsonResponse({'error': 'Failed to update, cannot add more products than are available'}, safe=False)
        cart_contains.Quantity += 1
    elif action == 'remove':
        cart_contains.Quantity -= 1
    elif quantity == 0:
        cart_contains.Quantity = 0
    else:
        return JsonResponse({'error': 'Failed to update, unknown action'}, safe=False)
    # Cart successfully updated hereafter
    # remove item from cart if  it's quantity is 0 after add/remove
    if cart_contains.Quantity == 0:
        cart.ItemsInCart.remove(cart_contains)
        cart_contains.delete()
        cart.save()
    else:
        cart_contains.save()
        cart.save()
    if request.path == '/cart/edit_item':
        return render(request, )
    return JsonResponse('Item updated', safe=False)


def get_or_create_cart(customer):
    try:
        cart = ShoppingCart.objects.get(SessionID=customer.session_key)
    except ShoppingCart.DoesNotExist:
        cart = ShoppingCart(SessionID=customer)
        cart.save()
    return cart


def get_or_create_cart_contains(product, cart, customer):
    # get the instance that's being changed from shoppingcart.itemsincart with the itemid, or create a new one
    try:
        items_in_cart = cart.ItemsInCart.all()
        # cart_contains = items_in_cart.filter(ItemID=product.ItemID)
        cart_contains = items_in_cart.filter(ItemID=product.ItemID)[0]
    except (CartContains.DoesNotExist, IndexError) as e:
        cart_contains = CartContains(ItemID=product, Quantity=0)
        cart_contains.save()
        cart.ItemsInCart.add(cart_contains)
        cart.save()
    return cart_contains
