from rest_framework import  serializers
from impiegato.models import Impiegato

class ImpiegatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Impiegato
        fields = '__all__'


