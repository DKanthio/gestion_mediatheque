# Generated by Django 5.0.2 on 2024-02-25 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliothecaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='livre',
            old_name='titre',
            new_name='nom',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='genre',
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour', models.DateField(blank=True, null=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_bibliothecaire.livre')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_bibliothecaire.media')),
            ],
        ),
    ]