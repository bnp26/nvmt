# Generated by Django 2.0.7 on 2018-08-17 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psych', '0004_auto_20180814_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('created', 'id')},
        ),
    ]
