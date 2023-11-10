from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.db.models import Max
from autopulse.settings import BASE_DIR


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def shopkeeper_registration(request):
    return render(request, 'shopkeeper_registration.html')


def shopkeeper_login(request):
    return render(request, 'shopkeeper_login.html')


def shopkeeper_home(request):
    return render(request, 'shopkeeper_home.html')


def tech_registration(request):
    return render(request, 'tech_registration.html')


def tech_login(request):
    return render(request, 'tech_login.html')


def tech_home(request):
    return render(request, 'tech_home.html')


def user_registration(request):
    return render(request, 'user_registration.html')


def user_login(request):
    return render(request, 'user_login.html')


def user_home(request):
    return render(request, 'user_home.html')


def contact(request):
    return render(request, 'contact.html')
