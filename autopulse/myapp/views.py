from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import User, Technician, myadmin, Shopkeeper, Login, ShopProduct, Cart, Career
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
        owner_name = request.POST['oname']
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
        username = request.POST['uname']
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
            request.session['shopkeeperusername'] = username
            return redirect('/shopkeeper_home')
            # Perform necessary actions after successful login
            return redirect('/')
        except Dealer.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('/shopkeeper_login')
    else:
        return render(request, 'shopkeeper_login.html')


def shopkeeper_home(request):
    if 'shopkeeperusername' in request.session:
        username = request.session['shopkeeperusername']
        a = Shopkeeper.objects.get(username=username)
    return render(request, 'shopkeeper_home.html', {'user': a})


def addproduct(request):
    if request.method == 'POST':
        username = request.session['shopkeeperusername']
        a = Shopkeeper.objects.get(username=username)

        p_name = request.POST['product_name']
        p_spec = request.POST['product_specification']
        manufacture_name = request.POST['manufacture_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        # print(request.FILES)
        abc = request.FILES.get('product_image')
        # p_image = request.POST['product_image']
        status = request.POST['status']

        new_product = ShopProduct(
            shopkeeper=a,
            product_name=p_name,
            product_specification=p_spec,
            manufacture_name=manufacture_name,
            price=price,
            quantity=quantity,
            product_image=abc,
            status=status
        )

        # Save the product to the database
        new_product.save()

        request.session['product_registration_success'] = True

        # Redirect to a success page or any other logic
        return redirect('shopkeeper_home')

        # Handle the case for GET requests
    return render(request, 'addproduct.html')


def manage_products(request):
    if 'shopkeeperusername' in request.session:
        username = request.session['shopkeeperusername']

        # Assuming the logged-in user is a shopkeeper
        logged_in_shopkeeper = get_object_or_404(Shopkeeper, username=username)
        print("hh", logged_in_shopkeeper)
        # Retrieve products for the logged-in shopkeeper
        products = ShopProduct.objects.filter(shopkeeper=logged_in_shopkeeper)
        print(products)

        return render(request, 'manage_product.html', {'products': products})


def shoplogout(request):
    logout(request)
    return redirect('index')


def updateit(request):
    if request.method == "POST":
        id = request.POST['id']
        p_name = request.POST['product_name']
        p_spec = request.POST['product_specification']
        manufacture_name = request.POST['manufacture_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        # print(request.FILES)
        abc = request.FILES.get('product_image')
        # p_image = request.POST['product_image']
        status = request.POST['status']

        prod = ShopProduct.objects.get(pk=id)
        print(prod)
        prod.product_name = p_name
        prod.product_specification = p_spec
        prod.manufacture_name = manufacture_name
        prod.price = price
        prod.quantity = quantity
        prod.product_image = abc
        prod.status = status
        prod.save()
        return redirect('manage_products')


def updateproduct(request):
    if request.method == "POST":
        id = request.POST['product_id']
        product = ShopProduct.objects.get(id=id)
        print(product)
        return render(request, 'updatepro.html', {'product': product})


class RemoveProductView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')

        try:
            product = ShopProduct.objects.get(id=product_id)
            product.delete()
            messages.success(request, 'Product removed successfully.')
        except ShopProduct.DoesNotExist:
            messages.error(request, 'Product does not exist.')

        return redirect('manage_products')


def tech_registration(request):
    if request.method == 'POST':
        tech_name = request.POST['tname']
        place = request.POST['place']
        city = request.POST['city']
        district = request.POST['dist']
        pincode = request.POST['pincode']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['uname']
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
        return redirect('/tech_login')
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
            return redirect('tech_home')
            # Perform necessary actions after successful login
            return redirect('/')
        except Technician.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('tech_login')
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
            # user=auth.authenticate(username=username,password=password)
            # auth.login(request,user)
            return redirect('/user_home')
            # Perform necessary actions after successful login
            # return redirect('/')
        except:
            context = {'msg': 'Invalid username or password'}
            return redirect('/user_login', context)
    else:
        return render(request, 'user_login.html')


def user_home(request):
    # Fetch all active products from the database
    products = ShopProduct.objects.filter(status='available')

    # Pass the products to the template
    return render(request, 'user_home.html', {'products': products})


def technicians(request):
    technician = Technician.objects.all()

    # Pass the products to the template
    return render(request, 'technicians.html', {'technician': technician})


def career(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = Career.objects.get(pk=id)

        username = request.user.username
        # User_model=User.objects.get(username=username)
        if request.user in name.candidate_name.all():
            name.candidate_name.remove(request.user)
            name.save()
            return redirect('career')
        else:
            name.candidate_name.add(request.user)
            name.save()
            return redirect('career')
    career = Career.objects.all()

    # Pass the products to the template
    return render(request, 'career.html', {'career': career})


def Productview(request, pk):
    products = ShopProduct.objects.get(pk=pk)
    if request.method == 'POST':
        qty = int(request.POST.get('qty', 1))
        cart_item, created = Cart.objects.get_or_create(product=products)
        cart_item.quantity += qty
        cart_item.save()

    return render(request, 'product.html', {'products': products})


def view_cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})


def contact(request):
    return render(request, 'contact.html')


def userlogout(request):
    logout(request)
    return redirect('index')
