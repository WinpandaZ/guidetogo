# Generated by Django 4.1.3 on 2022-11-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_auto_20221110_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]