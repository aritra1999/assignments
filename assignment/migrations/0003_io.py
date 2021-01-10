# Generated by Django 3.1.4 on 2021-01-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20210109_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='IO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intput1', models.TextField(blank=True, null=True)),
                ('intput2', models.TextField(blank=True, null=True)),
                ('intput3', models.TextField(blank=True, null=True)),
                ('intput4', models.TextField(blank=True, null=True)),
                ('intput5', models.TextField(blank=True, null=True)),
                ('output1', models.TextField(blank=True, null=True)),
                ('output2', models.TextField(blank=True, null=True)),
                ('output3', models.TextField(blank=True, null=True)),
                ('output4', models.TextField(blank=True, null=True)),
                ('output5', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=10, null=True)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignment.question')),
            ],
        ),
    ]