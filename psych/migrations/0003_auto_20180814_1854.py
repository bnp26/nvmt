# Generated by Django 2.0.7 on 2018-08-14 22:54

from django.db import migrations, models
import psych.models


class Migration(migrations.Migration):

    dependencies = [
        ('psych', '0002_auto_20180813_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.CharField(default=psych.models._createId, max_length=16, primary_key=True, serialize=False),
        ),
    ]