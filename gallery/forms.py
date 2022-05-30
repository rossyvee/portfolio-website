from django.forms import ModelForm
from .models import Image, Category, Location

from django import forms


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
