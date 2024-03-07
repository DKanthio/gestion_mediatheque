# Generated by Django 5.0.2 on 2024-03-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliothecaire', '0016_remove_membre_bloque_emprunteur_en_retard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunteur',
            name='en_retard',
        ),
        migrations.AddField(
            model_name='membre',
            name='bloque',
            field=models.BooleanField(default=False),
        ),
    ]
