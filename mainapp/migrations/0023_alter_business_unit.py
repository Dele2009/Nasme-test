# Generated by Django 4.1 on 2024-10-03 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_alter_business_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.unit'),
        ),
    ]
