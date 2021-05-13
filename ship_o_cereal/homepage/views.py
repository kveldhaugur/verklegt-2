from django.shortcuts import render
from django.http import HttpResponse
from main.models import Items
import random
from main.models import Items, ItemCategory

# Create your views here.
def index(request):
    context = {'items': Items.objects.all().order_by('Name')}
    context['cereal_category'], context['merch_category'], context['book_category'] = get_category_pics()
    context['popular'] = [get_random_item(Items.objects.all()) for _ in range(3)]
    context['daily_deals'] = [get_random_item(Items.objects.all()) for _ in range(3)]
    return render(request, 'homepage/index.html', context)


def get_category_pics():
    cereal_tag = ItemCategory.objects.get(CategoryTag='Cereal')
    merch_tag = ItemCategory.objects.get(CategoryTag='Merch')
    book_tag = ItemCategory.objects.get(CategoryTag='Book')
    cereals = Items.objects.filter(Tags=cereal_tag)
    merch = Items.objects.filter(Tags=merch_tag)
    books = Items.objects.filter(Tags=book_tag)
    cereal_rand_4 = []
    merch_rand_4 = []
    book_rand_4 = []
    for _ in range(4):
        cereal_rand_4.append(get_random_item(cereals).Image)
        merch_rand_4.append(get_random_item(merch).Image)
        book_rand_4.append(get_random_item(books).Image)
    return cereal_rand_4, merch_rand_4, book_rand_4


def get_random_item(query):
    return Items.objects.get(ItemID=random.choice(query).ItemID)

