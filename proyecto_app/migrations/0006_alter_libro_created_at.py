# Generated by Django 4.2.2 on 2023-06-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0005_alter_biblioteca_id_alter_imprenta_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
