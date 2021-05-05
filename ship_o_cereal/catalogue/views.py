from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main.models import Items



# Create your views here.

def index(request):
    context = {'items' : Items.objects.all().order_by('Name')}
    return render(request, 'catalogue/index.html', context)


def get_item_by_id(request, id):
    return render(request, 'catalogue/item-details.html', {
        'item': get_object_or_404(Items, pk=id)
    })
