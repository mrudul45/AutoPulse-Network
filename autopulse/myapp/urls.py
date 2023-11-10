"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('tech_registration', views.tech_registration, name='tech_registration'),
    path('shopkeeper_registration', views.shopkeeper_registration, name='shopkeeper_registration'),
    path('user_registration', views.user_registration, name='user_registration'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('user_login', views.user_login, name='user_login'),
    path('shopkeeper_login', views.shopkeeper_login, name='shopkeeper_login'),
    path('tech_login', views.tech_login, name='tech_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('user_home', views.user_home, name='user_home'),
    path('shopkeeper_home', views.shopkeeper_home, name='shopkeeper_home'),
    path('tech_home', views.tech_home, name='tech_home'),
    path('contact', views.contact, name='contact'),

]
