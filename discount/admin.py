from django.contrib import admin
from discount.models import DiscountData
from django.utils import timezone   

from .forms import ManagersForm


@admin.register(DiscountData)
class DiscountDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'id_DO', 'startDate', 'endDate', 'isDone']
    fieldsets = [
        ('Основная информация', {'fields': ['title', 'id_DO', 'slug', 'startDate', 'endDate']}),
        ('Дополнительная', {'fields': ['description']}),
        ('Служебная', {'fields': ['manager', 'shops', 'files', 'isDone', 'idDoneDate', ]})
    ]
    prepopulated_fields = {"slug": ("title",)}
    form = ManagersForm
    
    def save(isDone, isDoneDate):
        if isDoneDate == '2000-01-01':
            pass
        else:
            isDone = True
        super.save(isDone, isDoneDate)
        
