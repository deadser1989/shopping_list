from rest_framework import serializers
from api.models import User, Product, ShopList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopList
        fields = '__all__'