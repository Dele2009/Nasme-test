# Generated by Django 4.1 on 2024-10-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_alter_businessimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_type',
            field=models.CharField(choices=[('i', 'info'), ('w', 'warning'), ('e', 'error')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
