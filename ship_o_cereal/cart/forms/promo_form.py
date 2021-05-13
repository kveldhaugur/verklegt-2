from django import forms
from main.models import PromoCodes



class Promo(forms.Form):
    Name = forms.CharField()

