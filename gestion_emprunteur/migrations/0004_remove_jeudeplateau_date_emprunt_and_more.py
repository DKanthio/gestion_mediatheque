# Generated by Django 5.0.2 on 2024-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_emprunteur', '0003_cd_dvd_emprunteur_jeudeplateau_livre_delete_media_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jeudeplateau',
            name='date_emprunt',
        ),
        migrations.RemoveField(
            model_name='jeudeplateau',
            name='disponible',
        ),
        migrations.RemoveField(
            model_name='jeudeplateau',
            name='emprunteur',
        ),
        migrations.AddField(
            model_name='emprunteur',
            name='bloque',
            field=models.BooleanField(default=False),
        ),
    ]
