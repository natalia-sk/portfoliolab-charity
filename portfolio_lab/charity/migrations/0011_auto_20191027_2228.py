# Generated by Django 2.2.6 on 2019-10-27 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0010_auto_20191020_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='picked_up',
            field=models.DateTimeField(null=True),
        ),
    ]