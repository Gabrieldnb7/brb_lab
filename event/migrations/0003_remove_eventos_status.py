# Generated by Django 5.2 on 2025-06-10 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='status',
        ),
    ]
