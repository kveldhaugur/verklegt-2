from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('edit_item/', views.update_item, name='edit-cart')
]