from django import forms

# from .models import Product


class Product_form(forms.Form):
    product_name = forms.CharField(max_length=30)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    vendor = forms.CharField(max_length=30)
    quantity = forms.IntegerField()
    warranty = forms.IntegerField()
