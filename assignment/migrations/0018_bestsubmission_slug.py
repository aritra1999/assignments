# Generated by Django 3.1.4 on 2021-01-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0017_remove_bestsubmission_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsubmission',
            name='slug',
            field=models.SlugField(blank=True, max_length=11, null=True),
        ),
    ]