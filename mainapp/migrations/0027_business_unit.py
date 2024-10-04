# Generated by Django 4.1 on 2024-10-03 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_remove_business_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.unit'),
        ),
    ]
