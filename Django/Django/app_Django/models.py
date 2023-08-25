from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()
class Advertisements(models.Model):

    title = models.CharField('Загаловок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=13, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователи', on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='Django/')
    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price})"
    class Meta:
        db_table = 'Advertisements'
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
