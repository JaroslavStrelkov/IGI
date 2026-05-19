from django.contrib import admin
from .models import PromoCode

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'discount_percent', 'is_active', 'valid_until',)
    list_filter = ('is_active',)
    search_fields = ('code',)