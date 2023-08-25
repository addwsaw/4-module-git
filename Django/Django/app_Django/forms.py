from django import forms
from django.db import models
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, FileInput
class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=64)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    image = models.ImageField("изображение")
class AdvertisementsForms(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control form-control-lg'})
        }