# Generated by Django 5.0.6 on 2024-05-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='password_hash',
            field=models.CharField(max_length=255),
        ),
    ]
