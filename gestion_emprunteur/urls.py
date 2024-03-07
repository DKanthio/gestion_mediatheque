from django.urls import path
from . import views
from gestion_bibliothecaire.views import liste_medias
urlpatterns = [
 path('liste_medias/', liste_medias, name='liste_medias'),
]
