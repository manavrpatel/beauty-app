from rest_framework.serializers import ModelSerializer
from .models import Service, Booking

class ServiceCreate(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {'id': {'required': False}}
    

class BookingCreate(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {'booking_id': {'required': False}}
