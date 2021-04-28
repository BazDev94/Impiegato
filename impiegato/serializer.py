from rest_framework import  serializers
from .models import Impiegato

class ImpiegatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impiegato
        fields = '__all__'