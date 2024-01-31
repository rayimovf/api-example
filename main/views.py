from itertools import product

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Deliver, ProductItem
from .serializer import CategorySerializer, ProductSerializer, DeliverSerializer, ProductItemSerializer


class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateDeliver(CreateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer


class CreateProductItem(CreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


@api_view(['GET'])  #3
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    products = Product.objects.filter(category_id=category)
    total_products = products.count()
    total_price = sum(product.price for product in products)

    data = {
        'category_id': category.id,
        'total_products': total_products,
        'total_price': total_price,
    }

    return Response(data, status=status.HTTP_200_OK)


class ProductItemListAPIView(generics.ListAPIView):  #4
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Product.objects.filter(id=product_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_id'] = self.kwargs['product_id']
        return context





