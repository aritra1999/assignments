# Generated by Django 3.1.4 on 2020-12-27 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20201227_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='class_slug',
            new_name='class_name',
        ),
    ]
