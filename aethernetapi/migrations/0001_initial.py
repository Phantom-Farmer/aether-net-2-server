# Generated by Django 4.1.5 on 2023-01-27 21:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('image_url', models.URLField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('last_login', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Sleep_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('mind', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=500)),
                ('meditation', models.CharField(max_length=50)),
                ('favorite', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aethernetapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='SC_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleep_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aethernetapi.sleep_card')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aethernetapi.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Dream_Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('sleep_review', models.CharField(max_length=500)),
                ('dream', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aethernetapi.user')),
                ('sleep_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aethernetapi.sleep_card')),
            ],
        ),
    ]
