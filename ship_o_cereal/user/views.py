from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms.user_form import NewUserForm
from django.contrib import messages
# Create your views here.


def signup(request):
    context = {}
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('homepage-index')
        else:
            context['register_form'] = form
        #messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
        context['register_form'] = form
    return render(request=request, template_name='signup/index.html', context={
        'register_form': form
    })

def signin(request):
    return render(request, 'signin/index.html')

def logout(request):
    pass
