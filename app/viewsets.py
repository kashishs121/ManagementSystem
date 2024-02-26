from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
# from rest_framework import filters
class UserSignUpView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        # return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)zz

        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(generics.CreateAPIView):
  
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        # user = serializer.save()
       
        validated_data = serializer.validated_data
        username = validated_data.get('username')
        password = validated_data.get('password')
       
        # username = request.data.get('username')
        # password = request.data.get('password')
        # import pdb
        # pdb.set_trace()
        # print(f"Attempting login for username: {username}, password: {password}")
        # print(f"Request data: {request.data}")
        user = authenticate(username=username, password=password)
        # print(f"Authenticated user: {user}")
        
        # user = Users.objects.get(username=request.data['username'])
        # user = serializer.validated_data
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response_data = {
                'id': user.id,
                'username': user.username,
                'role': user.role,
                'token': token.key
            }
            # return Response({'token': token.key})
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Invalid credentials, return an appropriate response
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# class userviewsets(viewsets.ModelViewSet):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookHotel.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['booking_location', 'available_from', 'available']
    def get_queryset(self):
        queryset = super().get_queryset()
        bookinglocation = self.request.query_params.get('bookinglocation', None)

        if bookinglocation:
            queryset = queryset.filter(booking_location__icontains=bookinglocation)

        return queryset

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class SpecificBookingViewSet(viewsets.ModelViewSet):
    queryset = BookSpecificHotel.objects.all()
    serializer_class = SpecificBookingSerializer
    
    def book_hotel(self, request, *args, **kwargs):
        booknum = self.get_object()
        booked_on = request.data.get('booked')
        location = request.data.get('booking_location')
        
        if booknum.bookHotel.location==location and booknum.is_booked and booknum.available_from <= booked_on <= booknum.available:
            booknum.booked_dates = booked_on
            booknum.is_booked = False
            booknum.save()
            serializer = self.get_serializer(booknum)
            return Response(serializer.data)
        else:
            return Response("not booked for the specified date and location")