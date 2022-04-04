from django.shortcuts import render, reverse, redirect
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View,
)
from .models import Products


# create landing page view
class LandingPageView(TemplateView):
    template_name = "landing_page.html"


# product list view
class ProductsListView(ListView):
    template_name = "products/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Products.objects.all()


# product detail view
class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Products.objects.all()