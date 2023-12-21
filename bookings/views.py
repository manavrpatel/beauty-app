from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ServiceCreate, BookingCreate, BookingConfirm
from .models import Service, Booking
from django.db.models import Sum
from helpers.help import get_available_slots, get_end_time, convert_to_dmy
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime



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

        start_time = request.data.get('start_time')
        # print(start_time)
        # hour, minute = start_time.split(':')
        # print(f"Hour: {hour}, Minute: {minute}")

        services = request.data.get('services')
        service_arr = services.split(",")
        total_price = Service.objects.filter(name__in=service_arr).aggregate(total_price=Sum('price'))["total_price"]
        total_duration = Service.objects.filter(name__in=service_arr).aggregate(total_duration=Sum('duration'))["total_duration"]
        print(total_duration)
        end_time = get_end_time(start_time, total_duration)

        booking_info = {
            'user_id' : request.user.id ,
            'services' : request.data.get('services'),
            'price': total_price,
            'duration' : total_duration,
            'date' : request.data.get('date'),
            'start_time': start_time,
            'end_time' : end_time
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
        try:
            on_date = request.GET.get('date')
            today = str(timezone.now().date())
            print("today", today)
            # print(str(today))
            # print(on_date)
            on_date = convert_to_dmy(on_date)

            if on_date is None:
                raise ValidationError({"message": "Invalid date entered."})
            
            if str(today)>str(on_date):
                raise ValidationError({"message": "Invalid date entered."})
            
            services = request.GET.get('services').split(",")
            
            total_duration = Service.objects.filter(name__in=services).aggregate(total_duration=Sum('duration'))["total_duration"]
            curr_bookings = Booking.objects.filter(date=on_date).values('start_time', 'end_time').order_by('start_time')

            available_slots = {'slots' : get_available_slots(curr_bookings, total_duration), 'duration':total_duration}
            
            return JsonResponse(available_slots, status=status.HTTP_200_OK)

        except ValidationError as e:
            return JsonResponse(dict(e), status=400)
        
        except Exception as e:
            return JsonResponse({'message': f"Error in getting availability: {e}"}, status=500)
        
class BookingConfirmAPI(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Booking.objects.all()
    serializer_class = BookingConfirm
        

