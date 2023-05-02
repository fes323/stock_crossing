from django.contrib import admin
from discount.models import ActiveDiscount, BugsInDiscount, DiscountData, DiscountFiles, GalleryFilesWhithErrors, Promocode, PromocodeType

from .forms import DiscountForm, DiscountListForm, ManagersForm


class DiscountFilesInline(admin.TabularInline):
    fk_name = 'discount'
    model = DiscountFiles


@admin.register(DiscountData)
class DiscountDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'id_DO', 'startDate', 'endDate', 'isDone']
    fieldsets = [
        ('Основная информация', {'fields': ['title', 'id_DO', 'slug', 'startDate', 'endDate']}),
        ('Дополнительная', {'fields': ['description', 'type', 'discountSum', 'summation', 'discountThreshold', 'discountThresholdType', 'segment',]}),
        ('Служебная', {'fields': ['manager', 'shops', 'promocode', 'status', 'isDoneDate', 'createDate']}),
    ]
    readonly_fields = ['createDate', 'isDoneDate']
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
 
 
@admin.register(PromocodeType)
class PromocodeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    search_fields = ['promocode']


@admin.register(ActiveDiscount)
class ActiveDiscountAdmin(admin.ModelAdmin):
    list_display = ['date', 'count']
    search_fields = ['date']
    
    form = DiscountListForm
    
    
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from .models import ActiveDiscount, BugsInDiscount, DiscountData, Promocode
from shops.models import ShopManagers, Shop
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import SelectMultiple, Widget
from django.forms.widgets import TextInput
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class AddAnotherPopupIcon(Widget):
    """
    A Widget for displaying a green "plus" icon that opens a popup window to
    create a new related object.
    """
    template_name = 'django/forms/widgets/add_another_popup_icon.html'
    model_admin = None

    def __init__(self, model_admin, related_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_admin = model_admin
        self.related_model = related_model

    def get_related_url(self, info, action, *args):
        return reverse(
            f'admin:{info}_{action}',
            args=args,
        )

    def render(self, name, value, attrs=None, renderer=None):
        info = self.related_model._meta.app_label, self.related_model._meta.model_name
        url_params = self.get_related_url(info, 'add')
        related_url = f'{url_params}?_popup=1'
        context = {
            'related_url': related_url,
            'verbose_name': self.related_model._meta.verbose_name,
        }
        return mark_safe(render_to_string(self.template_name, context))

class ManagersForm(ModelForm):
    manager = forms.ModelMultipleChoiceField(
        queryset=ShopManagers.objects.all(),
        widget=FilteredSelectMultiple('Менеджеры', is_stacked=False)
    )
    shops = forms.ModelMultipleChoiceField(
        queryset=Shop.objects.all(),
        widget=FilteredSelectMultiple('Магазины', is_stacked=False)
    ) 
    promocode = forms.ModelMultipleChoiceField(
        queryset=Promocode.objects.all(),
        widget=FilteredSelectMultiple('Промокод', is_stacked=False)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add AddAnotherPopupIcon widget to 'manager' and 'promocode' fields
        self.fields['manager'].widget.add_another_icon = AddAnotherPopupIcon(
            model_admin=ShopManagersAdmin,
            related_model=ShopManagers,
        )
        self.fields['promocode'].widget.add_another_icon = AddAnotherPopupIcon(
            model_admin=PromocodeAdmin,
            related_model=Promocode,
        )
        