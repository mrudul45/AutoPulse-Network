from django.contrib import admin
from .models import Technician, Shopkeeper, User, ShopProduct,Career

# Register your models here.
admin.site.register(Technician)
admin.site.register(Shopkeeper)
admin.site.register(User)
admin.site.register(ShopProduct)
admin.site.register(Career)

