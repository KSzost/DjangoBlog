# Generated by Django 2.1.5 on 2019-01-21 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190121_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
