# Generated by Django 2.0.7 on 2018-08-29 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psych', '0005_auto_20180817_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('test_type', models.CharField(default='PNMT', max_length=45)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='Distributed', max_length=12)),
                ('completed', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='psych.Subject')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]