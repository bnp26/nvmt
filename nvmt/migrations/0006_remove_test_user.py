# Generated by Django 2.0.7 on 2018-08-14 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nvmt', '0005_auto_20180814_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
    ]
