# Generated by Django 3.1.2 on 2022-02-25 02:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0002_add_student_school_prefecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'places',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 2, 8, 51, 443295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 2, 8, 51, 443366, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ModelApp.places')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
    ]
