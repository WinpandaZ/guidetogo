# Generated by Django 4.1.3 on 2022-11-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='snippet',
            field=models.CharField(default='Click Link Above', max_length=255),
        ),
    ]