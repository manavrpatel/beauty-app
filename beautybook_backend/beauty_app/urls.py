from django.contrib import admin
from django.urls import path
from users.views.register import RegisterView
from users.views.login import LoginAPIView
from users.views.logout import LogoutAPIView
from bookings.views.service import ServiceAPI
from bookings.views.booking import BookingCreateAPI, BookingAvailabilityAPI, BookingConfirmAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

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
    path('booking/<uuid:pk>/', BookingConfirmAPI.as_view(), name='status'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
