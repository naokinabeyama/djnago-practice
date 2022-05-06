# Generated by Django 3.1.2 on 2022-03-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='誕生日'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.IntegerField(blank=True, null=True, verbose_name='性別'),
        ),
    ]