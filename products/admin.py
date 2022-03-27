from django.contrib import admin
from .models import Products


# register models in this app to admin
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'price')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name', 'category')
    list_per_page = 25


admin.site.register(Products, ProductsAdmin)

