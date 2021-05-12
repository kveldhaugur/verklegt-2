from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country, UserImage, ShoppingCart

# Create your views here.
def index(request):
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