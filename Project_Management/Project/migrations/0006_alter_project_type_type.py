# Generated by Django 5.0.4 on 2024-05-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_alter_estado_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_type',
            name='type',
            field=models.CharField(choices=[('Novo Levantamento', 'Novo Levantamento'), ('Novo PT Feeder ', 'Novo PT Feeder '), ('Levantamento Correction', 'Levantamento Correction'), ('Premisses Locked', ' Premisses Locked')], max_length=30, unique=True),
        ),
    ]
