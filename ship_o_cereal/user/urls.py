from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup-index'),
    path('signin', views.signin, name='signin-index'),
    path('logout', views.logout, name='logout-index')
]