# Generated by Django 5.0.4 on 2024-05-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_alter_project_type_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Submetido', 'Submetido'), ('Reijeitado', 'Reijeitado')], max_length=15, unique=True),
        ),
    ]
