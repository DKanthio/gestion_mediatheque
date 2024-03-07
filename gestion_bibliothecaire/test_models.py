from django.test import TestCase
from .models import Membre, Livre, DVD, CD, JeuDePlateau, Emprunt


class TestModels(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Test Membre")
        self.livre = Livre.objects.create(nom="Test Livre", auteur="Auteur Test")
        self.dvd = DVD.objects.create(nom="Test DVD", realisateur="Réalisateur Test")
        self.cd = CD.objects.create(nom="Test CD", artiste="Artiste Test")
        self.jeu = JeuDePlateau.objects.create(nom="Test Jeu", createur="Créateur Test")
        self.emprunt = Emprunt.objects.create(
            membre=self.membre,
            livre_emprunte=self.livre,
            dvd_emprunte=self.dvd,
            cd_emprunte=self.cd
        )

    def test_membre_creation(self):
        self.assertEqual(self.membre.nom, "Test Membre")

    def test_livre_creation(self):
        self.assertEqual(self.livre.nom, "Test Livre")
        self.assertEqual(self.livre.auteur, "Auteur Test")

    def test_dvd_creation(self):
        self.assertEqual(self.dvd.nom, "Test DVD")
        self.assertEqual(self.dvd.realisateur, "Réalisateur Test")

    def test_cd_creation(self):
        self.assertEqual(self.cd.nom, "Test CD")
        self.assertEqual(self.cd.artiste, "Artiste Test")

    def test_jeu_de_plateau_creation(self):
        self.assertEqual(self.jeu.nom, "Test Jeu")
        self.assertEqual(self.jeu.createur, "Créateur Test")

    def test_emprunt_creation(self):
        self.assertEqual(self.emprunt.membre, self.membre)
        self.assertEqual(self.emprunt.livre_emprunte, self.livre)
        self.assertEqual(self.emprunt.dvd_emprunte, self.dvd)
        self.assertEqual(self.emprunt.cd_emprunte, self.cd)
