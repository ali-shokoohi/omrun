# Generated by Django 2.2.2 on 2019-06-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190619_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='important',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='web.Employees'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='TasksPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Employees')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Tasks')),
            ],
        ),
    ]