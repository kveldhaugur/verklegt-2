from django.shortcuts import render
from django.http import HttpResponse
from main.models import Items


# Create your views here.
def index(request):
    context = {'Items': Items.objects.all().order_by('Name')}
    return render(request, 'homepage/index.html', context)