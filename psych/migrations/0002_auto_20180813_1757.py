# Generated by Django 2.0.7 on 2018-08-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psych', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaldiagnosis',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='psychdiagnosis',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
