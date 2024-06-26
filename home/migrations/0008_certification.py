# Generated by Django 4.2.9 on 2024-05-21 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_obtention', models.DateField()),
                ('fichier', models.FileField(upload_to='certifications/')),
                ('technologies_utilisees', models.CharField(blank=True, max_length=255)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
    ]
