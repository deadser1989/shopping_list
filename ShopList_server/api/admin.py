from django.contrib import admin
from .models import User, Product, ShopList

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'first_name', 'last_name', 'phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'quantity', 'units', 'buyer', 'price')

class ShopListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopList, ShopListAdmin)