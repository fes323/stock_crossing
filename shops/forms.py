from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm

from .models import Shop, ShopManagers


class ManagersForm(ModelForm):
    manager = forms.ModelMultipleChoiceField(
        queryset=ShopManagers.objects.all(),
        widget=FilteredSelectMultiple('Менеджеры', is_stacked=False)
    )

    class Meta:
        model = Shop
        fields = '__all__'

