# Generated by Django 2.0.7 on 2018-07-24 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('finish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_val', models.IntegerField(default=0)),
                ('y_val', models.IntegerField(default=0)),
                ('is_target', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True)),
                ('clicked_at', models.DateTimeField(blank=True)),
                ('click_time', models.DurationField(blank=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nvmt.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=2)),
                ('education', models.CharField(choices=[('HS', 'High School'), ('A', 'Associate Degree'), ('B', 'Bachelors Degree'), ('MS', 'Masters'), ('MD', 'Doctor of Medicin'), ('P', 'PhD')], default='HS', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nvmt.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trial_num', models.IntegerField(default=1)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nvmt.Test')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('tester', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ManyToManyField(to='nvmt.User'),
        ),
        migrations.AddField(
            model_name='card',
            name='trial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nvmt.Trial'),
        ),
    ]