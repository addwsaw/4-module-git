# Generated by Django 4.2.3 on 2023-08-10 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_Django', '0004_advertisements_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]
