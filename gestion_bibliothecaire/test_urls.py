from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(TestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.custom_login)

    def test_liste_emprunts_url(self):
        url = reverse('liste_emprunts')
        self.assertEqual(resolve(url).func, views.liste_emprunts)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.custom_logout)

    def test_liste_membres_url(self):
        url = reverse('liste_membres')
        self.assertEqual(resolve(url).func, views.liste_membres)

    def test_ajoutmembre_url(self):
        url = reverse('ajoutmembre')
        self.assertEqual(resolve(url).func, views.ajout_membre)

    def test_liste_medias_url(self):
        url = reverse('liste_medias')
        self.assertEqual(resolve(url).func, views.liste_medias)

    def test_ajouter_livre_url(self):
        url = reverse('ajouter_livre')
        self.assertEqual(resolve(url).func, views.ajouter_livre)

    def test_ajouter_dvd_url(self):
        url = reverse('ajouter_dvd')
        self.assertEqual(resolve(url).func, views.ajouter_dvd)

    def test_ajouter_cd_url(self):
        url = reverse('ajouter_cd')
        self.assertEqual(resolve(url).func, views.ajouter_cd)

    def test_ajouter_jeu_de_plateau_url(self):
        url = reverse('ajouter_jeu_de_plateau')
        self.assertEqual(resolve(url).func, views.ajouter_jeu_de_plateau)

    def test_liste_livres_url(self):
        url = reverse('liste_livres')
        self.assertEqual(resolve(url).func, views.liste_livres)

    def test_liste_dvds_url(self):
        url = reverse('liste_dvds')
        self.assertEqual(resolve(url).func, views.liste_dvds)

    def test_liste_jeux_url(self):
        url = reverse('liste_jeux')
        self.assertEqual(resolve(url).func, views.liste_jeux)

    def test_liste_cds_url(self):
        url = reverse('liste_cds')
        self.assertEqual(resolve(url).func, views.liste_cds)

    def test_emprunter_media_url(self):
        # Exemple d'une URL paramétrée
        url = reverse('emprunter_media', args=['livre', 1])
        self.assertEqual(resolve(url).func, views.emprunter_media)

    def test_confirmation_emprunt_url(self):
        url = reverse('confirmation_emprunt')
        self.assertEqual(resolve(url).func, views.confirmation_emprunt)

    def test_limite_emprunts_url(self):
        url = reverse('limite_emprunts')
        self.assertEqual(resolve(url).func, views.limite_emprunts)

    def test_emprunts_en_retard_url(self):
        url = reverse('emprunts_en_retard')
        self.assertEqual(resolve(url).func, views.emprunts_en_retard)

    def test_mettre_a_jour_membre_url(self):
        url = reverse('mettre_a_jour_membre', args=[1])
        self.assertEqual(resolve(url).func, views.mettre_a_jour_membre)

    def test_supprimer_membre_url(self):
        url = reverse('supprimer_membre', args=[1])
        self.assertEqual(resolve(url).func, views.supprimer_membre)
