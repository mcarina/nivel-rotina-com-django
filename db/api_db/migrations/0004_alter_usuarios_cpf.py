# Generated by Django 5.0.6 on 2024-05-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0003_alter_usuarios_password_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]