# Generated by Django 4.1 on 2024-09-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_user_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Businesses'},
        ),
        migrations.AlterModelOptions(
            name='businessimages',
            options={'verbose_name': 'Business Image', 'verbose_name_plural': 'Business Images'},
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'Social', 'verbose_name_plural': 'Socials'},
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='businessimages',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AddField(
            model_name='business',
            name='units',
            field=models.ManyToManyField(related_name='units', to='mainapp.unit'),
        ),
    ]
