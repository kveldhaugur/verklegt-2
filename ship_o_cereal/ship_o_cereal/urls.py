"""ship_o_cereal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('cart/', include('cart.urls')),
    path('help/', include('help.urls')),
    path('contactus/', include('contactus.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('checkout/', include('checkout.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('user/', include('user.urls')),
    path('recent_purchases/',include('recent_purchases.urls')),
]

handler404 = 'ship_o_cereal.views.error_404'
handler500 = 'ship_o_cereal.views.error_500'
handler403 = 'ship_o_cereal.views.error_403'
handler400 = 'ship_o_cereal.views.error_400'

