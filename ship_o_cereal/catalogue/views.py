import django.db.models.fields.related_descriptors
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from catalogue.forms.item_form import ItemCreateForm
from main.models import Items, ItemCategory


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = []
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

    context = {'items': Items.objects.all().order_by('Name'), 'tags': ItemCategory.objects.all().order_by('CategoryID')}
    return render(request, 'catalogue/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'catalogue/item-details.html', {
        'item': get_object_or_404(Items, pk=id)
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
