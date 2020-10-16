# Generated by Django 3.1.1 on 2020-09-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('leave', models.IntegerField(blank=True, default=4)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('approve', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]