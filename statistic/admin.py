from django.contrib import admin
from .models import CurrentDiscountPerDay


@admin.register(CurrentDiscountPerDay)
class CurrentDiscountPerDayAdmin(admin.ModelAdmin):
    list_display = ['day', 'discountCounter']
    search_fields = ['day']