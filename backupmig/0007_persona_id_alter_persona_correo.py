# Generated by Django 5.2.1 on 2025-06-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_producto_tienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Correo'),
        ),
    ]
