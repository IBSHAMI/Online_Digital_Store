from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import LandingPageView
from django.conf.urls.static import static
from .views import (
    ProductsListView,
)


app_name = 'products'


urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
]