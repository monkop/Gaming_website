# Generated by Django 3.0.4 on 2020-04-15 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='age',
        ),
    ]
