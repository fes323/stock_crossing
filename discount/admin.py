from django.contrib import admin
from discount.models import DiscountData

from .forms import ManagersForm


@admin.register(DiscountData)
class DiscountDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'id_DO', 'startDate', 'endDate', 'isDone']
    fieldsets = [
        ('Основная информация', {'fields': ['title', 'id_DO', 'startDate', 'endDate']}),
        ('Дополнительная', {'fields': ['description']}),
        ('Служебная', {'fields': ['manager', 'shops', 'files', 'isDone']})
    ]
    form = ManagersForm
