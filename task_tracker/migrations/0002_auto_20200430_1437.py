# Generated by Django 3.0.5 on 2020-04-30 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='task_title',
        ),
    ]
