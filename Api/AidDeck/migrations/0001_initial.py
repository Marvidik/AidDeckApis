# Generated by Django 4.1 on 2022-10-14 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FundApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('images', models.ImageField(upload_to='location_images')),
            ],
        ),
        migrations.CreateModel(
            name='Missionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('moi', models.ImageField(upload_to='IDS')),
                ('denomenational_affliation', models.CharField(max_length=100)),
                ('Gname', models.CharField(max_length=100)),
                ('Gemail', models.EmailField(max_length=254)),
                ('Gphone_number', models.IntegerField()),
                ('Gaddress', models.CharField(max_length=100)),
                ('Gnationality', models.CharField(max_length=100)),
                ('Gmoi', models.ImageField(upload_to='IDS')),
                ('Gdenomenational_affliation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('account_num', models.IntegerField()),
                ('account_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
