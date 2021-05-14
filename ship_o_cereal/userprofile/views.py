from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import UserInfo, Country, UserImage
from .forms.edit_user import UserEditForm, ChangeImage

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
    context["user_image"] = get_image(request.user.id)
    return render(request, 'userprofile/index.html', context)


def edit_info(request):
    context = {}
    id = int(str(request.user.id))
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
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
    context["user_image"] = get_image(id)
    context["edit_form"] = form
    return render(request, 'userprofile/edit.html', context)

def change_image(request):
    context = {}
    if request.method == "POST":
        form = ChangeImage(request.POST)
        if form.is_valid():
            image = form.cleaned_data.get("Image")
            id = int(str(request.user.id))
            a = UserImage(
                User=User.objects.get(id=id),
                Image=image
            )
            a.save()
            return redirect('edit-profile-index')
    else:
        form = ChangeImage()
    context['change_image_form'] = form
    return render(request, 'userprofile/changeimage.html', context)


def get_image(id):
    """
    Takes in user's id, tries to get his image if he has one,
    returns the image if it's found,
    returns none if there is no image for this user
    """
    try:
        image_obj = UserImage.objects.get(User=id)
        image = image_obj.Image
    except UserImage.DoesNotExist:
        image = None
    return image