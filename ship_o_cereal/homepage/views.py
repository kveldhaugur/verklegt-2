from django.shortcuts import render
from django.http import HttpResponse

cereals = [
    {'name': 'cheerios', 'price': 349},
    {'name': 'lucky charms', 'price': 345}
]

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', context={ 'cereals': cereals })