from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    # User data
    id = models.BigIntegerField(primary_key=True, blank=False, null=False) # == telegram_id
    user_name = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    # Сomparison with tables
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.user_name


class Product(models.Model):
    # Product data
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    units = models.CharField(max_length=100, blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_buyer', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class ShopList(models.Model):
    # ShopList data
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)

    # Сomparison with tables
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shoplist_owner')
    participants = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.name
