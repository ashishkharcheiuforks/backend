# Generated by Django 2.1.7 on 2019-06-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploytodotaskerapp', '0015_auto_20190628_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytmhistory',
            name='resultStatus',
            field=models.CharField(default='unrecognized', max_length=30, verbose_name='STATUS'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='STATUS',
            field=models.CharField(max_length=30, verbose_name='STATUS'),
        ),
    ]
