# Generated by Django 3.0.3 on 2020-03-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_new', '0015_auto_20200319_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
