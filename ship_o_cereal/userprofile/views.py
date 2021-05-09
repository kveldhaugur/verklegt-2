from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country

# Create your views here.
def index(request):
    context= {
        'message': None,
        'data': None
    }
    if request.user.is_authenticated:
        #account = User.objects.get(id=request.user.id)
        try:
            usrdata = UserInfo.objects.get(AccountConnected=request.user.id)
            info = {
                'firstname': usrdata.FirstName,
                'lastname': usrdata.LastName,
                'city' : usrdata.City,
                'postalcode': usrdata.PostalCode,
                'address': usrdata.Address,
                'housenum': usrdata.HouseNum,
                'mobilephone': usrdata.MobilePhone,
                'email': usrdata.Email,
                'ssn': usrdata.SSN,
                'country': 'Testvariable'
            }
        except UserInfo.DoesNotExist:
            info = None
        context['data'] = info
    else:
        return redirect('homepage-index')
    return render(request, 'userprofile/index.html', context)