from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country, UserImage, ShoppingCart, PromoCodes
import re
import datetime

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        # validate user and creditcard
        result, message = validate_payment(request.POST)
        #confirmation page goes here

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

    if request.session.session_key != None:
        try:
            cart = ShoppingCart.objects.get(SessionID=request.session.session_key)
        except ShoppingCart.DoesNotExist:
            cart = None
        if cart != None:
            cart_contains = cart.ItemsInCart.all()
            items = []
            for cart_item in cart_contains:
                item = cart_item.ItemID
                items.append((item, cart_item.Quantity))
            context['items_in_cart'] = items
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