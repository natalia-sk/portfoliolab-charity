# Generated by Django 2.2.6 on 2019-10-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0009_donation_is_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(),
        ),
    ]
