# Generated by Django 5.0.4 on 2024-05-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_projecto_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecto',
            name='perfil',
        ),
    ]