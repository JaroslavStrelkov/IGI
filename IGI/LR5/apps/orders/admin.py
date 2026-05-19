from django.contrib import admin
from .models import (Order, OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'employee', 'status', 'total_price', 'sale_date',)
    list_filter = ('status', 'sale_date',)
    search_fields = ('customer__username',)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'car', 'quantity', 'price',)