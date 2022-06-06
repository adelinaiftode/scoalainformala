from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Min, Max
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect

from aplicatie1.models import Product, Category


def get(request):
    print(request.user)
    return Response({'succes': "Esti autentificat"})


class DemoView(APIView):
    permission_classes = [IsAuthenticated]


def about(request):
    return render(request, "about.html")


# Product List
def product_list(request):
    total_data = Product.objects.count()
    data = Product.objects.all().order_by('-id')
    min_price = Product.objects.aggregate(Min('price'))
    max_price = Product.objects.aggregate(Max('price'))
    return render(request, 'shop.html',
                  {
                      'data': data,
                      'total_data': total_data,
                      'min_price': min_price,
                      'max_price': max_price,
                  }
                  )


# Product List According to Category
def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'shop.html', {
        'data': data,
    })


def home(request):
    data = Product.objects.filter().order_by('-id')
    return render(request, 'home.html', {'data': data, 'banners': {}})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]

    return render(request, 'shop.html',
                  {'data': product, 'related': related_products})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


