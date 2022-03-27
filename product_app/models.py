from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=30)
    quantity = models.IntegerField()
    warranty = models.IntegerField()

    def __str__(self):
        return self.product_name
