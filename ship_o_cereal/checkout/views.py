from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country, UserImage, ShoppingCart, PromoCodes, Order, OrderContains, Items
from django.contrib.sessions.models import Session
import re
import datetime

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        # validate user and creditcard
        result, message = validate_payment(request.POST)
        if result:
            # throw it all into an order
            order_id = create_order(request)
            return receipt(request, order_id) # receipt page goes here
        else:
            context['erroruser'] = message['user']
            context['errorcc'] = message['cc']

    context['data'] = None
    try:
        usrdata = UserInfo.objects.get(AccountConnected=request.user.id)
        info = {
            'firstname': usrdata.FirstName,
            'lastname': usrdata.LastName,
            'city': usrdata.City,
            'postalcode': usrdata.PostalCode,
            'address': usrdata.Address,
            'housenum': usrdata.HouseNum,
            'mobilephone': usrdata.MobilePhone,
            'email': usrdata.Email,
            'ssn': usrdata.SSN,
            'country': usrdata.Country
        }
    except UserInfo.DoesNotExist:
        info = {
            'firstname': '',
            'lastname': '',
            'city': '',
            'postalcode': '',
            'address': '',
            'housenum': '',
            'mobilephone': '',
            'email': '',
            'ssn': '',
            'country': ''
        }
    context['data'] = info
    context['countries'] = Country.objects.all()

    if request.session.session_key is not None:
        try:
            cart = ShoppingCart.objects.get(SessionID=request.session.session_key)
        except ShoppingCart.DoesNotExist:
            cart = None
        if cart is not None:
            cart_contains = cart.ItemsInCart.all()
            items = []
            total_price = 0
            i = 0
            for cart_item in cart_contains:
                item = cart_item.ItemID
                items.append((item, cart_item.Quantity))
                total_price += int(cart_item.Quantity) * item.Price
                i += 1 * cart_item.Quantity
            context['items_in_cart'] = items
            context['total_items'] = i
            if cart.Promo is not None:
                context['promo_name'] = cart.Promo.Name
                context['promo_val'] = int(round(cart.Promo.Discount*100))
                context['total'] = int(round((total_price * (1 - cart.Promo.Discount))))
            else:
                context['promo_name'] = None
                context['total'] = total_price
            return render(request, 'checkout/index.html', context)
    else:
        request.session.create()
    context['items_in_cart'] = None
    return render(request, 'checkout/index.html', context)


def validate_payment(post):
    credit_info = {}
    user_info = {}
    message = {}
    for item in post:
        if item[0:2] == 'CC':
            credit_info[item] = post[item]
        else:
            user_info[item] = post[item]
    val_bool, message['user'] = validate_user(user_info)
    val_bool, message['cc'] = validate_cc(credit_info)
    if val_bool == False:
        return False, message
    return True, 'Validation successful'


def validate_user(user_info):
    # TODO: phone &  & city are yet to be validated
    valid = True
    message = {}
    if user_info['City'].replace(' ', '').isalpha() is False:
        valid = False
        message['City'] = 'City name must contain only letters'
    if user_info['SSN'].replace(' ', '').replace('-', '').isdigit() is False:
        valid = False
        message['SSN'] = 'Your social security number has to be a number, 10 digit long'
    if user_info['MobilePhone'].replace(' ', '').replace('-', '').isdigit() is False:
        valid = False
        message['MobilePhone'] = 'Mobile phone must be a number'
    if user_info['FirstName'].replace(' ', '').isalpha() is False:
        valid = False
        message['FirstName'] = 'Firstname has to be letters only'
    if user_info['LastName'].replace(' ', '').isalpha() is False:
        valid = False
        message['LastName'] = 'Lastname has to be letters only'
    email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(email_regex, user_info['Email'])) is False:
        valid = False
        message['Email'] = 'Email was not valid'
    if user_info['Address'].replace(' ', '').isalpha() is False:
        valid = False
        message['Address'] = 'Address has to be letters only (house number is separated)'
    if user_info['HouseNum'].isdigit() is False:
        valid = False
        message['HouseNum'] = 'House number is not a number'
    # No need to check country, because its selection only
    if user_info['PostalCode'].isdigit() is False:
        valid = False
        message['PostalCode'] = 'ZIP/postal code is not a number'
    if valid:
        return valid, 'user info validated'
    else:
        return valid, message


def validate_cc(credit_info):
    valid = True
    message = {}
    if credit_info['CCName'].replace(' ', '').isalpha() is False:
        valid =  False
        message['CCName'] = 'Credit Card Name contains bad chars'
    if validate_creditcard(credit_info['CCNum']) is False:
        valid = False
        message['CCNum'] = 'bad creditcard number'
    if (credit_info['CCsecnum'].isdigit() is False) or ((len(credit_info['CCsecnum']) == 3) is False):
        valid = False
        message['CCsecnum'] = 'bad security number'
    if credit_info['CCexpM'].isdigit():
        if credit_info['CCexpY'].isdigit():
            cardyear = int(credit_info['CCexpY'])
            cardmonth = int(credit_info['CCexpM'])
            year, month = str(datetime.datetime.today()).split(' ')[0].split('-')[0:2]
            year = int(year)
            month = int(month)
            if cardyear >= year:
                return valid, message
            elif cardyear == year:
                if cardmonth >= month:
                    return valid, message
    message['CCexp'] = 'Credit card expiry date must be a number and it cannot be already expired'
    return False, message


def validate_creditcard(cardnum):
    if '-' in cardnum:
        cardnum = cardnum.replace("-", " ")
    cardnum = cardnum.replace(' ', '')
    if len(cardnum) == 16:
        if cardnum.isdigit():
            return True
    return False


def create_order(request):
    cart = ShoppingCart.objects.get(SessionID=request.session.session_key)
    itemsincart = cart.ItemsInCart.all()
    user = None
    order_items = []
    total_price = 0
    for item in itemsincart:
        product = Items.objects.get(ItemID=item.ItemID_id)
        order_item = OrderContains(Quantity=item.Quantity, ItemID=product)
        product.Quantity_available -= item.Quantity
        total_price += item.Quantity * product.Price
        product.save()
        if cart.Promo is not None:
            order_item.Price = round((product.Price * (1 - cart.Promo.Discount)), 2)
        else:
            order_item.Price = product.Price
        order_item.save()
        order_items.append(order_item)
    if cart.Promo is not None:
        total_price = int(round((total_price * (1 - cart.Promo.Discount))))
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        try: # to get user info
            shippinginfo = UserInfo.objects.get(AccountConnected=user)
        except UserInfo.DoesNotExist:
            shippinginfo = create_shipping_info(request.POST, user=user)
    else:
        shippinginfo = create_shipping_info(request.POST, user=None)
    order = Order(ShippingInfoID=shippinginfo, TotalPrice=total_price) # 'total' may be subject to change
    order.save()
    for item in order_items:
        order.ItemsInOrder.add(item)
    if user is not None:
        order.AccountConnected = user
    order.SessionConnected = Session.objects.get(session_key=request.session.session_key)
    order.save()
    #delete from cart
    for item in itemsincart:
        cart.ItemsInCart.remove(item)
        item.delete()
    cart.delete()
    return order.id



def create_shipping_info(post, user=None):
    country = Country.objects.get(CountryName=post['Country'])
    shippinginfo = UserInfo(
        AccountConnected=user,
        FirstName=post['FirstName'],
        LastName=post['LastName'],
        City=post['City'],
        PostalCode=post['PostalCode'],
        Address=post['Address'],
        HouseNum=post['HouseNum'],
        MobilePhone=post['MobilePhone'],
        Email=post['Email'],
        SSN=post['SSN'],
        Country=country
    )
    shippinginfo.save()
    return shippinginfo


def receipt(request, id):
    # first of all check if order exists
    context = {}
    # find the owner of the receipt
    try:
        session = Session.objects.get(session_key=request.session.session_key)
        user = User.objects.get(id=request.user.id)
        order = Order.objects.get(id=id, AccountConnected=user)
    except Session.DoesNotExist:
        # gtfo, no business here
        return redirect("homepage-index")
    except User.DoesNotExist:
        # try to get from session instead
        try:
            order = Order.objects.get(id=id, SessionConnected=session)
        except Order.DoesNotExist:
            # request doesnt have the right session or the account, so go to homepage jail
            return redirect("homepage-index")
    except Order.DoesNotExist:
        return redirect("homepage-index")
    context['order'] = order
    context['days_left'] = (datetime.datetime.now() + datetime.timedelta(days=7) - datetime.datetime.now()).days
    context['shipping'] = order.ShippingInfoID
    itemsinorder = order.ItemsInOrder.all()
    items = []
    total_items = 0
    for item in itemsinorder:
        items.append((item.Quantity, item.Price, Items.objects.get(ItemID=item.ItemID_id)))
        total_items += item.Quantity
    context['items'] = items
    context['total_items'] = total_items
    return render(request, 'checkout/receipt.html', context)
