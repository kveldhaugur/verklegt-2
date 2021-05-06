from django import forms
from django.forms import ModelForm, widgets
from main.models import Items


class ItemCreateForm(ModelForm):
    ManID_id = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Items
        exclude = ['ItemID', 'id_ManID_id']
        widgets = {
            'Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'Description': widgets.TextInput(attrs={'class': 'form-control'}),
            'Quantity_available': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Price': widgets.NumberInput(attrs={'class': 'form-control'})
        }
