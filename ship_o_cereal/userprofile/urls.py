from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='userprofile-index'),
    path('edit', views.edit_info, name='edit-profile-index'),
    path('changeimage', views.change_image, name='change-image')
]