from django.contrib import admin
from discount.models import BugsInDiscount, DiscountData, DiscountFiles, GalleryFilesWhithErrors
from django.utils import timezone   

from .forms import DiscountForm, ManagersForm


class DiscountFilesInline(admin.TabularInline):
    fk_name = 'discount'
    model = DiscountFiles

@admin.register(DiscountData)
class DiscountDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'id_DO', 'startDate', 'endDate', 'isDone']
    fieldsets = [
        ('Основная информация', {'fields': ['title', 'id_DO', 'slug', 'startDate', 'endDate']}),
        ('Дополнительная', {'fields': ['description']}),
        ('Служебная', {'fields': ['manager', 'shops', 'idDoneDate', ]}),
    ]
    list_filter = ['startDate', 'endDate', 'isDone']
    search_fields = ['title', 'id_DO']
    prepopulated_fields = {"slug": ("title",)}
    form = ManagersForm
    inlines = [DiscountFilesInline,]
    

class GalleryFilesWhithErrors(admin.TabularInline):
    fk_name = 'bug'
    model = GalleryFilesWhithErrors

@admin.register(BugsInDiscount)    
class BugsInDiscountAdmin(admin.ModelAdmin):
    search_fields = ['title']
    form = DiscountForm
    inlines = [GalleryFilesWhithErrors,]
    
    