from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginAPIView, LogoutAPIView
from bookings.views import ServiceAPI, BookingCreateAPI, BookingAvailabilityAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('service/', ServiceAPI.as_view(), name='service'),
    path('booking/', BookingCreateAPI.as_view(), name='booking'),

    path('booking/availability/', BookingAvailabilityAPI.as_view(), name='availability'),
]


# GET /booking/availability?start_date=”20-12-2023” & services=”Makeup,Eyebrow”