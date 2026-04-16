from rest_framework import viewsets
from .models import Auteur, Livre, Emprunt, Etiquette
from .serializers import (
    AuteurSerializer,
    LivreSerializer,
    EmpruntSerializer,
    EtiquetteSerializer
)


class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer


class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer


class EtiquetteViewSet(viewsets.ModelViewSet):
    queryset = Etiquette.objects.all()
    serializer_class = EtiquetteSerializer