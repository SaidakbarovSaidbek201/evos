from django.contrib import admin
from .models import Category, Product, Order, Customer, Cart, CartItem
# Register your models here.

admin.site.register(Category)
admin.site.register(Product) 
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
