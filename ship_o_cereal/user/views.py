from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms.user_form import NewUserForm, LoginUserForm
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
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
        context['register_form'] = form
    return render(request=request, template_name='signup/index.html', context={
        'register_form': form
    })


def signin(request):
    context= {}
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage-index")
        messages.error(request, "Invalid username or password.")
    else:
        form = LoginUserForm()
    context["signin_form"] = form
    return render(request, 'signin/index.html', context=context)


def logout_view(request):
    logout(request)
    return redirect("homepage-index")