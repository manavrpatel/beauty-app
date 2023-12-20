from rest_framework.serializers import ModelSerializer
from .models import Service

class ServiceCreate(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {'id': {'required': False}}
    
