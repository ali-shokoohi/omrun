# Generated by Django 2.1.7 on 2019-05-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_geographical_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='author',
            new_name='user',
        ),
    ]
