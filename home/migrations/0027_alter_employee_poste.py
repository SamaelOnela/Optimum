# Generated by Django 4.2.9 on 2024-05-22 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_projet_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='poste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.poste'),
        ),
    ]
