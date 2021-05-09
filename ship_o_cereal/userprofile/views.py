from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country
from .forms.edit_user import UserEditForm

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
                'country': usrdata.Country
            }
        except UserInfo.DoesNotExist:
            info = None
        context['data'] = info
    else:
        return redirect('homepage-index')
    return render(request, 'userprofile/index.html', context)


def edit_info(request):
    context = {}
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            id = int(str(request.user.id))
            try:
                b = UserInfo.objects.get(AccountConnected=id)
                b.delete()
            except UserInfo.DoesNotExist:
                pass
            a = UserInfo(
                AccountConnected=User.objects.get(id=id),
                FirstName=form.cleaned_data.get('FirstName'),
                LastName=form.cleaned_data.get('LastName'),
                City=form.cleaned_data.get('City'),
                PostalCode=form.cleaned_data.get('PostalCode'),
                Address=form.cleaned_data.get('Address'),
                HouseNum=form.cleaned_data.get('HouseNum'),
                MobilePhone=form.cleaned_data.get('MobilePhone'),
                Email=form.cleaned_data.get('Email'),
                SSN=form.cleaned_data.get('SSN'),
                Country=form.cleaned_data.get('Country')
            )
            a.save()
            return redirect('userprofile-index')
    else:
        form = UserEditForm()
    context["edit_form"] = form
    return render(request, 'userprofile/edit.html', context)


#def signin(request):
#    context= {}
#    if request.method == "POST":
#        form = LoginUserForm(request, data=request.POST)
#        if form.is_valid():
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                login(request, user)
#                messages.info(request, f"You are now logged in as {username}.")
#                return redirect("homepage-index")
#        messages.error(request, "Invalid username or password.")
#    else:
#        form = LoginUserForm()
#    context["signin_form"] = form
#    return render(request, 'signin/index.html', context=context)