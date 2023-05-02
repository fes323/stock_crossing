from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm

from .models import ActiveDiscount, BugsInDiscount, DiscountData, Promocode
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
    promocode = forms.ModelMultipleChoiceField(
        queryset=Promocode.objects.all(),
        widget=FilteredSelectMultiple('Промокод', is_stacked=False)
    )

    class Meta:
        model = DiscountData
        fields = '__all__'
        
class DiscountForm(ModelForm):
    discount = forms.ModelMultipleChoiceField(
        queryset=DiscountData.objects.all(),
        widget=FilteredSelectMultiple('Акции', is_stacked=False)
    )
    
    class Meta:
        model = BugsInDiscount
        fields = '__all__'
    
    
class DiscountListForm(ModelForm):
    discount_data = forms.ModelMultipleChoiceField(
        queryset=DiscountData.objects.all(),
        widget=FilteredSelectMultiple('Акции', is_stacked=False)
    )

    class Meta:
        model = ActiveDiscount
        fields = '__all__'
