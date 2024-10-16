# Generated by Django 4.1 on 2024-10-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0032_message_message_type_message_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
