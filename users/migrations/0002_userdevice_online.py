# Generated by Django 4.0.1 on 2022-03-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdevice',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
