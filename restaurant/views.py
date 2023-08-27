from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import Menu
# Create your views here.
def index(request):
    return render(request, 'home.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer