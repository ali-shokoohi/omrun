# Generated by Django 2.1.7 on 2019-06-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20190601_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
