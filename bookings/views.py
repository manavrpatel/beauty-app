from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ServiceCreate, BookingCreate
from .models import Service, Booking
from django.db.models import Sum



# Create your views here.
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
    
class BookingCreateAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request,  *args, **kwargs):

        services = request.data.get('services')
        service_arr = services.split(",")
        total_price = Service.objects.filter(name__in=service_arr).aggregate(total_price=Sum('price'))["total_price"]
        total_duration = Service.objects.filter(name__in=service_arr).aggregate(total_duration=Sum('duration'))["total_duration"]

        booking_info = {
            'user_id' : request.user.id ,
            'services' : request.data.get('services'),
            'price': total_price,
            'duration' : total_duration,
            'date' : request.data.get('date'),
            'start_time': request.data.get('start_time')
        }  

        serializer = BookingCreate(data=booking_info)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class GetBookingDetailsAPI(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request,  *args, **kwargs):
#         book_id = request.GET.get('id')
    
#         return Response(book_id, status=status.HTTP_200_OK)
    
class BookingAvailabilityAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,  *args, **kwargs):

