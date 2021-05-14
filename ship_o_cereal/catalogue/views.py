import django.db.models.fields.related_descriptors
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from catalogue.forms.item_form import ItemCreateForm
from main.models import Items, ItemCategory, SessionHistory
from django.contrib.sessions.models import Session
import json


# Create your views here.
def index(request):
    print(request.POST)
    recentSearch = ''
    recentTag = ''
    if 'recentSearch' in request.POST:
        recentSearch = request.POST['recentSearch']
    if 'recentTag' in request.POST:
        recentTag = request.POST['recentTag']
    if 'search_filter' in request.POST:
        search_filter = request.POST['search_filter']
        add_to_history(request.session, search_filter)
        recentTag = ''
        context = {
            'items': Items.objects.filter(Name__icontains=search_filter),
            'tags': ItemCategory.objects.all().order_by('CategoryID'),
            'recentSearch': search_filter,
            'recentTag': recentTag
        }
        return render(request, 'catalogue/index.html', context)
    else:
        context = {
            'items': Items.objects.all().order_by('Name'),
            'tags': ItemCategory.objects.all().order_by('CategoryID'),
            'recentSearch': recentSearch,
            'recentTag': recentTag
        }
    if 'filter-by' in request.POST or 'filter-by' in request.GET:
        tag_filter = None
        if 'filter-by' in request.GET:
            filter_filter = request.GET['filter-by']
            tag_filter = ItemCategory.objects.get(CategoryTag=filter_filter)
        else:
            filter_filter = request.POST['filter-by']
        if 'recentSearch' in request.POST and request.POST['recentSearch'] != '':
            items = Items.objects.filter(Name__icontains=request.POST['recentSearch'])
        else:
            items = Items.objects.all()
        if tag_filter is None:
            tag_filter = ItemCategory.objects.get(CategoryID=int(filter_filter))
        context = {
            'items': items.filter(Tags=tag_filter),
            'tags': ItemCategory.objects.all(),
            'recentSearch': recentSearch,
            'recentTag': tag_filter.CategoryTag
        }
    return render(request, 'catalogue/index.html', context)

def get_tags(request):
    items_lis = []
    items = Items.objects.all()
    if request.GET['recentSearch'] != '':
        items = items.filter(Name__icontains=request.GET['recentSearch'])
    if request.GET['recentTag'] != '':
        tag = ItemCategory.objects.get(CategoryTag=request.GET['recentTag'])
        items = items.filter(Tags=tag)
    for x in items:
        tags = []
        for tag in x.Tags.all():
            tags.append(tag.CategoryID)
        ble = {
            'ItemID': x.ItemID,
            'Name': x.Name,
            'Description': x.Description,
            'Image': x.Image,
            'Price': x.Price,
            'Tags': tags
        }
        items_lis.append(ble)
    return JsonResponse({'data': items_lis})

def add_to_history(session, searchstr):
    if session.session_key == None:
        session.create()
    if searchstr != "" and searchstr != None:
        key = session.session_key
        user_sesh = Session.objects.get(session_key=key)
        try:
            SessionHistory.objects.get(SessionID=user_sesh, HistoryStr=searchstr)
        except SessionHistory.DoesNotExist:
            new_history = SessionHistory(SessionID=user_sesh, HistoryStr=searchstr)
            new_history.save()


def get_item_by_id(request, id):
    item = get_object_or_404(Items, pk=id)

    tags = []
    for tag in item.Tags.all():
        tags.append(tag.CategoryTag)
    retItem = {
        'ItemID': item.ItemID,
        'Name': item.Name,
        'Manufacturer': item.ManID,
        'Description': item.Description,
        'Image': item.Image,
        'Price': item.Price,
        'Image_extra': item.Image_extra,
        'Tags': tags
    }
    return render(request, 'catalogue/item-details.html', {
        'item': retItem
    })

def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('catalogue-index')

    else:
        form = ItemCreateForm()
    return render(request, 'catalogue/create_item.html', {
        'form': form
    })
