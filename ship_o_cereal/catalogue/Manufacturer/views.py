from django.shortcuts import render

Manufacturers = [
    {'ManID': 1, 'Name': 'General Mills'},
    {'ManID': 2, 'Name': 'Nabisco'},
    {'ManID': 3, 'Name': 'Kellogg\'s'},
    {'ManID': 4, 'Name': 'Ralston'},
    {'ManID': 5, 'Name': 'Nestle'},
    {'ManID': 6, 'Name': 'Quaker'},
    {'ManID': 7, 'Name': 'Post Cereal'},
]
# Create your views here.

#No idea what render does but he does it in candy queen video so lets find out one day
    #UPDATE: I found out what render does, some html stuff we probably won't use :^)
    #TODO: remove this, probably
def index(request):
    return render(request, 'catalogue/Manufacturer/index.html', context={ Manufacturers })
