from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import ModelSerializer, BookingSerializer
from .permissions import IsVisitorForPostOnly
from rest_framework import viewsets


# Create your views here.


def index(request):
    return render(request, "index.html")


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsVisitorForPostOnly]


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]
