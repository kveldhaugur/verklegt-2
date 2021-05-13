from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='checkout-index'),
    path('receipt/<int:id>', views.receipt, name='receipt-index'),
]