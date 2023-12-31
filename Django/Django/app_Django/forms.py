from django import forms
from django.db import models
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, FileInput
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

def title_validator(value):
    if value[0] == '?':
        red_word = format_html('<span style="color: red; font-weight: bold;">Ошибка!</span>')
        error = _(f"{red_word} Заголовок не может начинаться со знака '?'")
        raise ValidationError(
            error,
            params={'value': value},
        )

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=64, validators=[title_validator])
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
