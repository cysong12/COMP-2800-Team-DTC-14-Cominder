# Generated by Django 3.0.5 on 2020-05-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]