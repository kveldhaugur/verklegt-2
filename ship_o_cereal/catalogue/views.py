import django.db.models.fields.related_descriptors
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from catalogue.forms.item_form import ItemCreateForm
from main.models import Items, ItemCategory, SessionHistory
from django.contrib.sessions.models import Session



# Create your views here.
def index(request):
    print(request.POST)
    if 'search_filter' in request.POST:
        search_filter = request.POST['search_filter']
        add_to_history(request.session, search_filter)

        context = {
            'items': Items.objects.filter(Name__icontains=search_filter),
            'tags': ItemCategory.objects.all().order_by('CategoryID'),
            'recentSearch': search_filter
        }

    else:
        context = {
            'items': Items.objects.all().order_by('Name'),
            'tags': ItemCategory.objects.all().order_by('CategoryID'),
            'recentSearch': ''
        }
    return render(request, 'catalogue/index.html', context)

def get_tags(request):
    items = []
    search_filter = ""
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
    for x in Items.objects.filter(Name__icontains=search_filter):
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
        items.append(ble)
    return JsonResponse({'data': items})

def add_to_history(session, searchstr):
    if session.session_key == None:
        session.create()
    if searchstr != "" and searchstr is not None:
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
        'Description': item.Description,
        'Image': item.Image,
        'Price': item.Price,
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
