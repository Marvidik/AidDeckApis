# Generated by Django 4.1 on 2022-10-15 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AidDeck', '0004_remove_missionary_email_remove_missionary_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
