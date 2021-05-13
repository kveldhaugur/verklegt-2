from django.shortcuts import render, redirect
from main.models import Order
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        orders = Order.objects.filter(AccountConnected=user)
        context['orders'] = orders
        return render(request, 'recent_purchases/index.html', context)
    return redirect('homepage/index.html')