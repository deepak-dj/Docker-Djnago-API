import json

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .forms import Product_form
from .models import Product
from .serializers import Product_serializer


# api code
class Product_view(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serializer


# Application code

def register_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(
            first_name=first_name,
            email=email,
            username=username,
            password=password
        )
        user.save()
        return redirect('login')

    else:
        return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")
    else:
        return render(request, "login.html")


def logout_view(request):
    auth.logout(request)
    return redirect("login")


@login_required(redirect_field_name="login")
def home_view(request):
    response = requests.get("http://127.0.0.1:8000/api_view/")
    if response.status_code == 200:

        context = {"product": json.loads(response.text)}
        return render(request, "home.html", context)
    else:
        context = {"error": "Sorry! Employees information not available"}
        return render(request, "home.html", context)


@login_required(redirect_field_name="login")
def create_view(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name", "")
        price = request.POST.get("price", "")
        vendor = request.POST.get("vendor", "")
        quantity = request.POST.get("quantity", "")
        warranty = request.POST.get("warranty", "")

        product = {
            "product_name": product_name,
            "price": price,
            "vendor": vendor,
            "quantity": quantity,
            "warranty": warranty,
        }
        response = requests.post("http://127.0.0.1:8000/api_view/",
                                 data=product)

        if response.status_code == 201:
            return redirect("home")
        else:
            return HttpResponse(response.text)

    else:
        form = Product_form()
        context = {"form": form}
        return render(request, "create_form.html", context)


@login_required(redirect_field_name="login")
def update_view(request, id):
    response = requests.get("http://127.0.0.1:8000/api_view/" + str(id) + "/")
    if response.status_code == 200:
        if request.method == "POST":
            product_name = request.POST.get("product_name", "")
            price = request.POST.get("price", "")
            vendor = request.POST.get("vendor", "")
            quantity = request.POST.get("quantity", "")
            warranty = request.POST.get("warranty", "")

            product = {
                "product_name": product_name,
                "price": price,
                "vendor": vendor,
                "quantity": quantity,
                "warranty": warranty,
            }
            response = requests.put(
                "http://127.0.0.1:8000/api_view/" + str(id) + "/", data=product
            )

            if response.status_code == 200:
                return redirect("home")
            else:
                return HttpResponse(response.text)

        else:
            form = json.loads(response.text)
            return render(request, "update.html", {"form": form})
    else:
        return HttpResponse(response.text)


@login_required(redirect_field_name="login")
def delete_view(request, id):
    response = requests.delete(
        "http://127.0.0.1:8000/api_view/" + str(id) + "/"
    )

    if response.status_code == 204:
        messages.info(request, "data deleted")
        return redirect("home")
    else:
        return HttpResponse("Data not available for delete")
