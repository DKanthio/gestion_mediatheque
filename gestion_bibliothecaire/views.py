import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Membre, Creationmembre, Livre, DVD, CD, JeuDePlateau, Emprunt
from datetime import timedelta, datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.utils import timezone



def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Utilisation de get() pour éviter les erreurs
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authentification de l'utilisateur
        if user is not None:
            login(request, user)  # Connexion de l'utilisateur
            return redirect('liste_emprunts')  # Redirection vers la page d'accueil après la connexion
        else:
            # Gérer les cas d'identification incorrecte
            error_message = 'Identifiants incorrects'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')


def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    membre.supprimer()
    return HttpResponseRedirect(reverse('liste_membres'))


def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'livres/liste_medias.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})


def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'livres/liste_emprunts.html', {'emprunts': emprunts})


def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'livres/liste_membres.html', {'membres': membres})


def ajout_membre(request):
    if request.method == 'POST':
        creationmembre = Creationmembre(request.POST)
        if creationmembre.is_valid():
            membre = Membre()
            membre.nom = creationmembre.cleaned_data['name']
            membre.save()
            membres = Membre.objects.all()
            return render(request, 'livres/liste_membres.html',
                          {'membres': membres})
    else:
        creationmembre = Creationmembre()
        return render(request,
                      'livres/creer_membre-emprunter.html',
                      {'creationLivre': creationmembre}
                      )


def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'livres/livre.html', {'livres': livres})


def liste_cds(request):
    cds = CD.objects.all()
    return render(request, 'livres/cd.html', {'cds': cds})


def liste_dvds(request):
    dvds = DVD.objects.all()
    return render(request, 'livres/dvd.html', {'dvds': dvds})


def liste_jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'livres/jeudeplateau.html', {'jeux': jeux})


def ajouter_livre(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        auteur = request.POST.get('auteur')
        Livre.objects.create(nom=nom, auteur=auteur)
        return redirect('liste_livres')
    return render(request, 'livres/ajouter_livre.html')


def ajouter_dvd(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        realisateur = request.POST.get('realisateur')
        DVD.objects.create(nom=nom, realisateur=realisateur)
        return redirect('liste_dvds')
    return render(request, 'livres/ajouter_dvd.html')


def ajouter_cd(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        artiste = request.POST.get('artiste')
        CD.objects.create(nom=nom, artiste=artiste)
        return redirect('liste_cds')
    return render(request, 'livres/ajouter_cd.html')


def ajouter_jeu_de_plateau(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        createur = request.POST.get('createur')
        JeuDePlateau.objects.create(nom=nom, createur=createur)
        return redirect('liste_jeux')
    return render(request, 'livres/ajouter_jeu_de_plateau.html')


def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    if request.method == 'POST':
        nouveau_nom = request.POST.get('nouveau_nom')
        membre.mettre_a_jour(nouveau_nom)
        return redirect('liste_membres')
    return render(request, 'livres/mettre_a_jour_membre.html', {'membre': membre})


def confirmation_emprunt(request):
    return render(request, 'livres/confirmation_emprunt.html')


def limite_emprunts(request):
    return render(request, 'livres/limite_emprunts.html')


def emprunts_en_retard(request):
    emprunts = Emprunt.objects.filter(date_retour__lt=timezone.now())
    return render(request, 'livres/page_des_emprunts_en_retard.html', {'emprunts': emprunts})


def emprunter_media(request, media_type, media_id):
    if request.method == 'POST':
        membre_id = request.POST.get('membre_id')
        membre = get_object_or_404(Membre, pk=membre_id)

        # Vérification de la limite d'emprunts par membre
        emprunts_actifs = Emprunt.objects.filter(membre_id=membre_id).count()
        if emprunts_actifs >= 3:
            return redirect('limite_emprunts')

        # Vérification des emprunts en retard du membre
        emprunts_en_retard = Emprunt.objects.filter(membre=membre, date_retour__lt=datetime.now())
        if emprunts_en_retard.exists():
            return redirect('emprunts_en_retard')

        # Vérification de la disponibilité du média
        media_id = request.POST.get('media_id')
        if media_type == 'livre':
            media = get_object_or_404(Livre, pk=media_id)
        elif media_type == 'dvd':
            media = get_object_or_404(DVD, pk=media_id)
        elif media_type == 'cd':
            media = get_object_or_404(CD, pk=media_id)
        else:

            pass

        if not media.disponible:
            return HttpResponseBadRequest("Ce média n'est pas disponible.")


        if media_type == 'livre':
            livre_emprunte = get_object_or_404(Livre, pk=media_id)
            Emprunt.objects.create(membre=membre, livre_emprunte=livre_emprunte, date_emprunt=timezone.now(),
                                   date_retour=timezone.now()
 + timedelta(days=7))

        elif media_type == 'dvd':
            dvd_emprunte = get_object_or_404(DVD, pk=media_id)
            Emprunt.objects.create(membre=membre, dvd_emprunte=dvd_emprunte, date_emprunt=timezone.now(),
                                   date_retour=timezone.now() + timedelta(days=7))

        elif media_type == 'cd':
            cd_emprunte = get_object_or_404(CD, pk=media_id)
            Emprunt.objects.create(membre=membre, cd_emprunte=cd_emprunte, date_emprunt=timezone.now(),
                                   date_retour=timezone.now() + timedelta(days=7))

        # Redirige l'utilisateur vers la page de confirmation d'emprunt
        return redirect('confirmation_emprunt')

    else:
        membres = Membre.objects.all()
        if media_type == 'livre':
            media = Livre.objects.all()
        elif media_type == 'dvd':
            media = DVD.objects.all()
        elif media_type == 'cd':
            media = CD.objects.all()
        else:
            # Gérer d'autres types de médias si nécessaire
            pass

        return render(request, 'livres/emprunter_media.html', {'membres': membres, 'media': media})
