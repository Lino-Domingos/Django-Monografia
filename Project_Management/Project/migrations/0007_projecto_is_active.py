# Generated by Django 5.0.4 on 2024-05-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0006_alter_project_type_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
