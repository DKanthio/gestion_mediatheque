from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Membre, Livre, DVD, CD, JeuDePlateau, Emprunt
from datetime import datetime, timedelta


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.membre = Membre.objects.create(nom="Test Membre")
        self.livre = Livre.objects.create(nom="Test Livre", auteur="Auteur Test")
        self.dvd = DVD.objects.create(nom="Test DVD", realisateur="Réalisateur Test")
        self.cd = CD.objects.create(nom="Test CD", artiste="Artiste Test")
        self.jeu = JeuDePlateau.objects.create(nom="Test Jeu", createur="Créateur Test")

    def test_custom_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logout.html')

    def test_custom_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_liste_medias_view(self):
        response = self.client.get(reverse('liste_medias'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/liste_medias.html')

    def test_liste_emprunts_view(self):
        response = self.client.get(reverse('liste_emprunts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/liste_emprunts.html')

    def test_liste_membres_view(self):
        response = self.client.get(reverse('liste_membres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/liste_membres.html')

    def test_ajout_membre_view(self):
        response = self.client.post(reverse('ajoutmembre'), {'name': 'Nouveau Membre'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Membre.objects.filter(nom='Nouveau Membre').exists())

    def test_liste_livres_view(self):
        response = self.client.get(reverse('liste_livres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/livre.html')

    def test_liste_cds_view(self):
        response = self.client.get(reverse('liste_cds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/cd.html')

    def test_liste_dvds_view(self):
        response = self.client.get(reverse('liste_dvds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/dvd.html')

    def test_liste_jeux_view(self):
        response = self.client.get(reverse('liste_jeux'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/jeudeplateau.html')

    def test_ajouter_livre_view(self):
        response = self.client.post(reverse('ajouter_livre'), {'nom': 'Nouveau Livre', 'auteur': 'Nouvel Auteur'})
        self.assertEqual(response.status_code, 302)  # Redirection après l'ajout
        self.assertTrue(Livre.objects.filter(nom='Nouveau Livre', auteur='Nouvel Auteur').exists())

    def test_ajouter_dvd_view(self):
        response = self.client.post(reverse('ajouter_dvd'),
                                    {'nom': 'Nouveau DVD', 'realisateur': 'Nouveau Réalisateur'})
        self.assertEqual(response.status_code, 302)  # Redirection après l'ajout
        self.assertTrue(DVD.objects.filter(nom='Nouveau DVD', realisateur='Nouveau Réalisateur').exists())

    def test_ajouter_cd_view(self):
        response = self.client.post(reverse('ajouter_cd'), {'nom': 'Nouveau CD', 'artiste': 'Nouvel Artiste'})
        self.assertEqual(response.status_code, 302)  # Redirection après l'ajout
        self.assertTrue(CD.objects.filter(nom='Nouveau CD', artiste='Nouvel Artiste').exists())

    def test_ajouter_jeu_de_plateau_view(self):
        response = self.client.post(reverse('ajouter_jeu_de_plateau'),
                                    {'nom': 'Nouveau Jeu', 'createur': 'Nouveau Créateur'})
        self.assertEqual(response.status_code, 302)  # Redirection après l'ajout
        self.assertTrue(JeuDePlateau.objects.filter(nom='Nouveau Jeu', createur='Nouveau Créateur').exists())

    def test_mettre_a_jour_membre_view(self):
        response = self.client.post(reverse('mettre_a_jour_membre', args=[self.membre.id]),
                                    {'nouveau_nom': 'Nouveau Nom'})
        self.assertEqual(response.status_code, 302)  # Redirection après la mise à jour
        self.assertTrue(Membre.objects.filter(nom='Nouveau Nom').exists())

    def test_confirmation_emprunt_view(self):
        response = self.client.get(reverse('confirmation_emprunt'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/confirmation_emprunt.html')

    def test_limite_emprunts_view(self):
        response = self.client.get(reverse('limite_emprunts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/limite_emprunts.html')

    def test_emprunts_en_retard_view(self):
        response = self.client.get(reverse('emprunts_en_retard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livres/page_des_emprunts_en_retard.html')


