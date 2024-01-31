from rest_framework import serializers
from .models import Category, Product, Deliver, ProductItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = '__all__'


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ProductItem
        fields = '__all__'

