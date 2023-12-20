from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginAPIView, LogoutAPIView
from bookings.views import ServiceAPI, BookingCreateAPI, GetBookingDetailsAPI
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

    # path('booking/availability/', GetBookingDetailsAPI.as_view(), name='availability'),
]
