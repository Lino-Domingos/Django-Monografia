# Generated by Django 5.0.4 on 2024-06-17 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_delete_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projecto',
            options={'ordering': ['equipe']},
        ),
    ]
