# admin.py
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_by')
    list_filter = ('category', 'price')


admin.site.register(Product, ProductAdmin)
