from rest_framework import generics
from rest_framework.response import Response
from .serializer import ImpiegatoSerializer
from .models import Impiegato

class PostApi(generics.CreateAPIView):
    queryset = Impiegato.objects.all()
    serializer_class = ImpiegatoSerializer

class GetApi(generics.ListAPIView):
    queryset = Impiegato.objects.all()
    serializer_class = ImpiegatoSerializer

class UpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Impiegato.objects.all()
    serializer_class = ImpiegatoSerializer

class DeleteApi(generics.DestroyAPIView):
    queryset = Impiegato.objects.all()
    serializer_class = ImpiegatoSerializer