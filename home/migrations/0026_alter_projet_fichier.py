# Generated by Django 4.2.9 on 2024-05-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_projet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='fichier',
            field=models.FileField(upload_to='projets/'),
        ),
    ]