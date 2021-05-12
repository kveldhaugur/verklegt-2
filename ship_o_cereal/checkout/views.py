from django.shortcuts import render
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
            #throw it all into an order
            create_order(request)
            return render(request, 'confirmation.html thingy')#confirmation page goes here

    else:
        context = {
            'data': None
        }
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
                context['total'] = round((total_price * (1 - cart.Promo.Discount)),2)
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
    for item in post:
        if item[0:2] == 'CC':
            credit_info[item] = post[item]
        else:
            user_info[item] = post[item]
    val_bool, message = validate_user(user_info)
    if val_bool == False:
        return False, message
    val_bool, message = validate_cc(credit_info)
    if val_bool == False:
        return False, message
    return True, 'Validation successful'


def validate_user(user_info):
    if user_info['FirstName'].isalpha() == False:
        return False, 'firstname contains bad chars'
    if user_info['LastName'].isalpha() == False:
        return False, 'lastname contains bad chars'
    email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(email_regex, user_info['Email'])) == False:
        return False, 'email was not valid'
    if user_info['Address'].isalpha() == False:
        return False, 'address contains bad chars'
    if user_info['HouseNum'].isdigit() == False:
        return False, 'housenum is not a number'
    # No need to check country, because its selection only
    if user_info['PostalCode'].isdigit() == False:
        return False, 'ZIP/postal code is not a number'
    return True, 'user info validated'


def validate_cc(credit_info):
    if credit_info['CCName'].isalpha() == False:
        return False, 'CCName contains bad chars'
    if validate_creditcard(credit_info['CCNum']) == False:
        return False, 'bad creditcard number'
    if (credit_info['CCsecnum'].isdigit() == False) or ((len(credit_info['CCsecnum']) == 3) == False):
        return False, 'bad security number'
    if credit_info['CCexpM'].isdigit():
        if credit_info['CCexpY'].isdigit():
            cardyear = int(credit_info['CCexpY'])
            cardmonth = int(credit_info['CCexpM'])
            year, month = str(datetime.datetime.today()).split(' ')[0].split('-')[0:2]
            year = int(year)
            month = int(month)
            if cardyear > year:
                return True, 'card validated'
            elif cardyear == year:
                if cardmonth >= month:
                    return True, 'card validated'
    return False, 'bad cc expiry date'


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
    order_items = []
    for item in itemsincart:
        product = Items.objects.get(ItemID=item.ItemID)
        order_item = OrderContains(Quantity=item.Quantity, ItemID=product)
        order_item.save()
        order_items.append(order_item)
    if request.user.is_authenticated():
        user = User.models.get(id=request.user.id)
        try: # to get user info
            shippinginfo = UserInfo.objects.get(AccountConnected=user)
        except UserInfo.DoesNotExist:
            shippinginfo = create_shipping_info(request.POST, user=user)
    else:
        shippinginfo = create_shipping_info(request.POST, user=None)
    order = Order(ShippingInfoID=shippinginfo, TotalPrice=request.POST['total']) # 'total' may be subject to change
    for item in order_items:
        order.ItemsInOrder.add(item)
    order.save()
    



def create_shipping_info(post, user=None):
    country = Country.objects.get(CountryName=post['Country'])
    shippinginfo = UserInfo(
        AccountConnected=user,
        FirstName=post['FirstName'],
        LastName=POST['LastName'],
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