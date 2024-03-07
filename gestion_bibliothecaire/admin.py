from django.contrib import admin
from .models import Emprunt, Emprunteur, Livre, DVD, CD, Membre, JeuDePlateau

# Enregistrez vos modèles ici
admin.site.register(Emprunt)
admin.site.register(Emprunteur)
admin.site.register(Livre)
admin.site.register(DVD)
admin.site.register(CD)
admin.site.register(Membre)
admin.site.register(JeuDePlateau)
