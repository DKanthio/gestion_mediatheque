# Generated by Django 5.0.2 on 2024-03-05 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_emprunteur', '0004_remove_jeudeplateau_date_emprunt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cd',
            name='emprunteur',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='emprunteur',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='emprunteur',
        ),
        migrations.DeleteModel(
            name='JeuDePlateau',
        ),
        migrations.DeleteModel(
            name='CD',
        ),
        migrations.DeleteModel(
            name='DVD',
        ),
        migrations.DeleteModel(
            name='Emprunteur',
        ),
        migrations.DeleteModel(
            name='Livre',
        ),
    ]
