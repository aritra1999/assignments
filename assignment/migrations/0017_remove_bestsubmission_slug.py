# Generated by Django 3.1.4 on 2021-01-10 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0016_auto_20210110_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestsubmission',
            name='slug',
        ),
    ]
