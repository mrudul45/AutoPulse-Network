from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class myadmin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Technician(models.Model):
    id = models.AutoField(primary_key=True)
    tech_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Shopkeeper(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    opent = models.TimeField()
    closet = models.TimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
