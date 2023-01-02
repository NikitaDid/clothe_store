from django.contrib import admin
from apps.catalog.models import Category

@admin.register(Category)
class CaregoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
