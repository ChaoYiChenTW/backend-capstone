from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import ModelSerializer, BookingSerializer
from .permissions import IsVisitorForPostOnly


# Create your views here.
class BookingItemView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsVisitorForPostOnly]


class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]
