
from rest_framework import serializers
from .models import record

class firstserializer(serializers.ModelSerializer):
    class Meta:
        model=record
        fields='__all__'


    

            