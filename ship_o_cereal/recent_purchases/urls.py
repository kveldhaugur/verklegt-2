from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/recent_purchases
    path('', views.index, name='index')
]

