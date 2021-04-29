
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .serializer import ImpiegatoSerializer
from impiegato.models import Impiegato

class ImpiegatoViewSet(viewsets.ModelViewSet):
    queryset = Impiegato.objects.all()
    serializer_class = ImpiegatoSerializer
     