# Generated by Django 5.0.4 on 2024-05-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0003_team_membros_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
