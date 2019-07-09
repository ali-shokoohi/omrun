# Generated by Django 2.2.2 on 2019-06-21 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20190620_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.TextField()),
                ('info', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('kind', models.TextField()),
                ('intent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.TextField()),
                ('photo', models.ImageField(default='default-plan.png', upload_to='')),
                ('data', models.TextField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Plans')),
            ],
        ),
        migrations.CreateModel(
            name='NotiPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Notifications')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]