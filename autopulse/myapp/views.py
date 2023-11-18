from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import User, Technician, myadmin, Shopkeeper, Login
from django.contrib import messages
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
    if request.method == 'POST':
        username = "admin"
        password = "admin"
        try:
            admin = myadmin.objects.get(username=username, password=password)
            return redirect('/admin_home')
        #  Perform necessary actions after successful login
        # return redirect('/')
        except myadmin.DoesNotExist:
            context = {'msg': 'Invalid username or password'}
            return redirect('/admin_login', context)

    else:
        return render(request, 'admin_login.html')


def admin_home(request):
       return render(request, 'admin_home.html')


def shopkeeper_registration(request):
    if request.method == 'POST':
        owner_name = request.POST['mname']
        shop_name = request.POST['shname']
        place = request.POST['place']
        city = request.POST['city']
        district = request.POST['dist']
        pincode = request.POST['pincode']
        contact = request.POST['contact']
        email = request.POST['email']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        opent = request.POST['opent']
        closet = request.POST['closet']
        username = request.POST['sname']
        password = request.POST['password']

        # Create a new Customer object and save it to the database
        new_shopkeeper = Shopkeeper(
            owner_name=owner_name,
            shop_name=shop_name,
            place=place,
            city=city,
            district=district,
            pincode=pincode,
            contact=contact,
            email=email,
            latitude=latitude,
            longitude=longitude,
            opent=opent,
            closet=closet,
            username=username,
            password=password  # Note: Password should be securely hashed before saving to the database
        )
        new_shopkeeper.save()
        messages.success(request, 'You have been successfully registered!')
        return redirect('/shopkeeper_login')
    else:

     return render(request, 'shopkeeper_registration.html')


def shopkeeper_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username and password match the database records
        try:
            shopkeeper = Shopkeeper.objects.get(username=username, password=password)
            messages.success(request, 'Login successful!')
            return redirect('/medicalshop_home')
            # Perform necessary actions after successful login
            return redirect('/')
        except Dealer.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('/medicalshop_login')
    else:
     return render(request, 'shopkeeper_login.html')


def shopkeeper_home(request):
    return render(request, 'shopkeeper_home.html')


def tech_registration(request):
    if request.method == 'POST':
        tech_name = request.POST['tname']
        place = request.POST['place']
        city = request.POST['city']
        district = request.POST['dist']
        pincode = request.POST['pincode']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['dsname']
        password = request.POST['password']

        # Create a new Customer object and save it to the database
        new_technician = Technician(
            tech_name=tech_name,
            place=place,
            city=city,
            district=district,
            pincode=pincode,
            contact=contact,
            email=email,
            username=username,
            password=password  # Note: Password should be securely hashed before saving to the database
        )
        new_technician.save()
        # user1 = User.objects.create_user(first_name=first_name,
        #                                  last_name=last_name,
        #                                  gender=gender,
        #                                  place=place,
        #                                  city=city,
        #                                  district=district,
        #                                  pincode=pincode,
        #                                  contact=contact,
        #                                  email=email,
        #                                  username=username,
        #                                  password=password)
        #
        # user1.save()
        messages.success(request, 'You have been successfully registered!')
        return redirect('/technician_login')
    else:
     return render(request, 'tech_registration.html')


def tech_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username and password match the database records
        try:
            technician = Technician.objects.get(username=username, password=password)
            messages.success(request, 'Login successful!')
            return redirect('/technician_home')
            # Perform necessary actions after successful login
            return redirect('/')
        except Technician.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('/technician_login')
    else:
     return render(request, 'tech_login.html')


def tech_home(request):
    return render(request, 'tech_home.html')


def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        place = request.POST['place']
        city = request.POST['city']
        district = request.POST['dist']
        pincode = request.POST['pincode']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['usname']
        password = request.POST['password']

        # Create a new Customer object and save it to the database
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            place=place,
            city=city,
            district=district,
            pincode=pincode,
            contact=contact,
            email=email,
            username=username,
            password=password  # Note: Password should be securely hashed before saving to the database
        )
        new_user.save()
        # user1 = User.objects.create_user(first_name=first_name,
        #                                  last_name=last_name,
        #                                  gender=gender,
        #                                  place=place,
        #                                  city=city,
        #                                  district=district,
        #                                  pincode=pincode,
        #                                  contact=contact,
        #                                  email=email,
        #                                  username=username,
        #                                  password=password)
        #
        # user1.save()

        return redirect('/user_login')
    else:
     return render(request, 'user_registration.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username and password match the database records
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('/user_home')
            # Perform necessary actions after successful login
            # return redirect('/')
        except:
            context = {'msg': 'Invalid username or password'}
            return redirect('/user_login', context)
    else:
     return render(request, 'user_login.html')


def user_home(request):
    return render(request, 'user_home.html')


def contact(request):
    return render(request, 'contact.html')
