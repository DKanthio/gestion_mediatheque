# Generated by Django 5.0.2 on 2024-03-03 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliothecaire', '0017_remove_emprunteur_en_retard_membre_bloque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='bloque',
        ),
        migrations.AddField(
            model_name='membre',
            name='emprunteur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion_bibliothecaire.emprunteur'),
        ),
    ]
