from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from bookings.serializers.service import ServiceCreate
from bookings.models.service import Service 

class ServiceAPI(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request,  *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceCreate(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,  *args, **kwargs):
        service_info={
            'name' : request.data.get('name') ,
            'price' : request.data.get('price') ,
            'duration' : request.data.get('duration') 
        }

        serializer = ServiceCreate(data=service_info)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)