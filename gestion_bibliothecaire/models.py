from django.db import models
from django.utils import timezone
from django import forms


class Emprunt(models.Model):
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)
    livre_emprunte = models.ForeignKey('Livre', on_delete=models.CASCADE, null=True, blank=True)
    dvd_emprunte = models.ForeignKey('DVD', on_delete=models.CASCADE, null=True, blank=True)
    cd_emprunte = models.ForeignKey('CD', on_delete=models.CASCADE, null=True, blank=True)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.membre} - {self.livre_emprunte} - {self.dvd_emprunte} - {self.cd_emprunte} - {self.date_emprunt} - {self.date_retour}"


class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)


class Creationmembre(forms.Form):
    name = forms.CharField(required=False)


class Emprunt_media(forms.Form):
    name = forms.CharField(required=False)


class Media(models.Model):
    nom = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class Livre(Media):
    auteur = models.CharField(max_length=100)


class DVD(Media):
    realisateur = models.CharField(max_length=100)


class CD(Media):
    artiste = models.CharField(max_length=100)


class JeuDePlateau(models.Model):
    nom = models.CharField(max_length=100)
    createur = models.CharField(max_length=100, blank=True, null=True)


class Membre(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"

    def mettre_a_jour(self, nouveau_nom):
        self.nom = nouveau_nom
        self.save()

    def supprimer(self):
        self.delete()
