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

    def __str__(self):
        return self.tech_name


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

    def __str__(self):
        return self.shop_name


class ShopProduct(models.Model):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE, default=1)
    product_name = models.CharField(max_length=255)
    product_specification = models.TextField()
    manufacture_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='pp_image', blank=True, null=True)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    product_name = models.ForeignKey('ShopProduct', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"

class Career(models.Model):
    job_name = models.CharField(max_length=255)
    job_description = models.CharField(max_length=255)
    candidate_name = models.ManyToManyField(User,related_name='Users')
    qualification = models.TextField()


    def __str__(self):
        return self.job_name
