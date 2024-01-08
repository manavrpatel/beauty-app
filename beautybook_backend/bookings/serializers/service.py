from rest_framework.serializers import ModelSerializer
from bookings.models.booking import Booking
from bookings.models.service import Service

class ServiceCreate(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {'id': {'required': False}}