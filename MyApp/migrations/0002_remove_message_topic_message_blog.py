# Generated by Django 5.2.4 on 2025-07-19 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='topic',
        ),
        migrations.AddField(
            model_name='message',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.blog'),
        ),
    ]
