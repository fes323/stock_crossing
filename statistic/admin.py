from django.contrib import admin
from .models import ActiveDiscount


@admin.register(ActiveDiscount)
class ActiveDiscountAdmin(admin.ModelAdmin):
    list_display = ['date', 'count']
    search_fields = ['date']