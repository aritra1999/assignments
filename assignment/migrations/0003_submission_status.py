# Generated by Django 3.1.4 on 2021-01-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20210111_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='status',
            field=models.CharField(blank=True, default='Wrong', max_length=7, null=True),
        ),
    ]
