# Generated by Django 4.2 on 2023-05-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='website',
            field=models.URLField(verbose_name='website'),
        ),
    ]