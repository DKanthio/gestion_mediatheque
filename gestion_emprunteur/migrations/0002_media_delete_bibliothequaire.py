# Generated by Django 5.0.2 on 2024-02-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_emprunteur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kanthio', max_length=100)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bibliothequaire',
        ),
    ]
