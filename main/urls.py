from django.urls import path
from .views import CreateCategory, CreateProduct, CreateDeliver, CreateProductItem, category_detail, ProductItemListAPIView

urlpatterns = [
    path('create-category/', CreateCategory.as_view()),
    path('create-product/', CreateProduct.as_view()),
    path('create-deliver/', CreateDeliver.as_view()),
    path('create-product-item/', CreateProductItem.as_view()),
    path('category-detail/<int:pk>/', category_detail, name='category-detail'),
    path('item-detail/<int:product_id>/', ProductItemListAPIView.as_view(), name='item-detail'),
]

