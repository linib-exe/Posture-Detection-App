# Generated by Django 5.1.1 on 2024-09-14 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esp32data',
            old_name='param1',
            new_name='accx',
        ),
        migrations.RenameField(
            model_name='esp32data',
            old_name='param2',
            new_name='accy',
        ),
        migrations.RenameField(
            model_name='esp32data',
            old_name='param3',
            new_name='accz',
        ),
        migrations.RemoveField(
            model_name='esp32data',
            name='param4',
        ),
        migrations.RemoveField(
            model_name='esp32data',
            name='param5',
        ),
    ]
