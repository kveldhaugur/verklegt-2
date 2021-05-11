from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country, UserImage

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
    return render(request, 'checkout/index.html', context)