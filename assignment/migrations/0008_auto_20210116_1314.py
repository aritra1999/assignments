# Generated by Django 3.1.4 on 2021-01-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_question_averagescore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='averageScore',
            new_name='average',
        ),
    ]
