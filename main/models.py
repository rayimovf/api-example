from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=5)
    barcode = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Deliver(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    deliver_id = models.ForeignKey(Deliver, on_delete=models.CASCADE)



