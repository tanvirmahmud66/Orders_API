from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdminView(admin.ModelAdmin):
    list_display = ('id','name','price')


class OrdersAdminView(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product', 'quantity','payment_info','created_at','updated_at')



admin.site.register(Product, ProductAdminView)
admin.site.register(Order, OrdersAdminView)
