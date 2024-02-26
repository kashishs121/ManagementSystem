from django.contrib import admin
from django.urls import path
from . import views
# from .views import UserRegistrationView, UserLoginView
from .views import *
from django.urls import path
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import HotelViewSet
from .viewsets import *
from django.urls import path
from .viewsets import UserSignUpView, UserLoginView

router_booking = DefaultRouter()
router_booking.register(r'hotels', BookingViewSet, basename='hotel')

router_bookhotels = DefaultRouter()
router_bookhotels.register(r'bookhotels', SpecificBookingViewSet, basename='bookhotels')

urlpatterns = [
    path('',views.index),
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('api/', include(router_booking.urls)),
    path('api/bookhotels',include(router_bookhotels.urls))
]

