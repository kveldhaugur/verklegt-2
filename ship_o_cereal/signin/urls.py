from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='signin-index'),
]
