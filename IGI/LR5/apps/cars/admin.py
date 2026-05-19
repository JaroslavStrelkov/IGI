from django.contrib import admin

from .models import (Manufacturer, CarCategory, Feature, Car)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    search_fields = ('name',)

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'category', 'price', 'year', 'is_available',)
    list_filter = ('category', 'manufacturer', 'fuel_type', 'transmission',)
    search_fields = ('name', 'manufacturer__name',)
    filter_horizontal = ('features',)
