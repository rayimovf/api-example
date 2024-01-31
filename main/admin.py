from django.contrib import admin
from .models import Category, Product, Deliver, ProductItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Deliver)
admin.site.register(ProductItem)
