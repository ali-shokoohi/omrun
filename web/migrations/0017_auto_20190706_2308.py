# Generated by Django 2.2.2 on 2019-07-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20190629_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
