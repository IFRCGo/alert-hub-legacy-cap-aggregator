# Generated by Django 4.2.2 on 2023-06-24 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cap_feed', '0005_alter_country_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='effective',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
