# Generated by Django 2.1.7 on 2019-05-03 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_geographical'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='geographical',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.Geographical'),
            preserve_default=False,
        ),
    ]
