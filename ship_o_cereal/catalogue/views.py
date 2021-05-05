from django.shortcuts import render
from django.http import HttpResponse
from main.models import *

# Create your views here.

def index(request):
    context = {'items' : Items.objects.all().order_by('Name')}
    return render(request, 'catalogue/index.html', context)

def all_items(request):
    context = {'items' : Items.objects.all().order_by('Name')}
    return render(request, 'catalogue/index.html', context)