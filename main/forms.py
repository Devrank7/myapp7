from django import forms
from django.forms import ModelForm

from main.models import Food


class PhytonForm(ModelForm):
    class Meta:
        model = Food
        fields = ["name", "price","grade"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'name'}),
            "price": forms.TextInput(attrs={'placeholder': 'price'}),
            "grade": forms.TextInput(attrs={'placeholder': 'grade'}),
        }
