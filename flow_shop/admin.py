from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('name', 'description')
