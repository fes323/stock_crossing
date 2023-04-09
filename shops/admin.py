from django.contrib import admin
from shops.models import ShopManagers, Shop, Notes
from shops.forms import ManagersForm


@admin.register(ShopManagers)
class ShopManagersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_manager']

    form = ManagersForm

    def display_manager(self, obj):
        return ", ".join([manager.name for manager in obj.manager.all()])

    display_manager.short_description = 'Менеджеры'


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    pass

