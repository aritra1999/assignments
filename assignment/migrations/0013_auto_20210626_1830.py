# Generated by Django 3.1.6 on 2021-06-26 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0012_auto_20210620_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='io',
            old_name='input1',
            new_name='input',
        ),
        migrations.RenameField(
            model_name='io',
            old_name='input2',
            new_name='output',
        ),
        migrations.RemoveField(
            model_name='io',
            name='input3',
        ),
        migrations.RemoveField(
            model_name='io',
            name='input4',
        ),
        migrations.RemoveField(
            model_name='io',
            name='input5',
        ),
        migrations.RemoveField(
            model_name='io',
            name='output1',
        ),
        migrations.RemoveField(
            model_name='io',
            name='output2',
        ),
        migrations.RemoveField(
            model_name='io',
            name='output3',
        ),
        migrations.RemoveField(
            model_name='io',
            name='output4',
        ),
        migrations.RemoveField(
            model_name='io',
            name='output5',
        ),
    ]
