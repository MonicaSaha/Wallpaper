from django import forms
from .models import *


class image_form(forms.ModelForm):
    image_url = forms.URLField(widget=forms.URLInput(), required=True, max_length=100000)

    class Meta():
        model = Image
        fields = ['image_url']


class category_form(forms.ModelForm):
    cat_name = forms.CharField(widget=forms.CharField(), required=True, max_length=1000)

    class Meta():
        model = Category
        fields = ['cat_name']
