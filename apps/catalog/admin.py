from django.contrib import admin
from apps.catalog.models import Category, Product


@admin.register(Category)
class CaregoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
