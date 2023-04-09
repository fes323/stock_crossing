from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm

from .models import DiscountData
from shops.models import ShopManagers, Shop


class ManagersForm(ModelForm):
    manager = forms.ModelMultipleChoiceField(
        queryset=ShopManagers.objects.all(),
        widget=FilteredSelectMultiple('Менеджеры', is_stacked=False)
    )
    shops = forms.ModelMultipleChoiceField(
        queryset=Shop.objects.all(),
        widget=FilteredSelectMultiple('Менеджеры', is_stacked=False)
    )

    class Meta:
        model = DiscountData
        fields = '__all__'
