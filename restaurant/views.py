import json
from django.views.decorators.csrf import csrf_exempt
from logging import warn
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu
from datetime import datetime
from .serializers import BookingSerializer, MenuSerializer
from .forms import BookingForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
@csrf_exempt
def bookings(request):
    if(request.methods == 'POST'):
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot = data['reservation_slot'].exists()
        )
        if(exist is False):
            booking = Booking(first_name=data['first_name'], 
                              reservation_date=data['reservation_date'], 
                              reservation_slot=data['reservation_slot'], )
            booking.save()
        else:
            return HttpResponse("{'error : 1}", content_type='application/json')
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')

@csrf_exempt
@csrf_exempt
def menu(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Create a new Menu item
            new_item = Menu.objects.create(
                title=data.get('title'),
                price=data.get('price'),
                inventory=data.get('inventory')
            )
            return JsonResponse(
                {"message": "Menu item created", "id": new_item.id},
                status=201
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    # For GET requests, render the 'menu.html' template
    menu_items = Menu.objects.all()
    
    # Because your template uses `menu.menu` in the loop,
    # we'll nest our items under a "menu" key
    main_data = {"menu": menu_items}
    return render(request, 'menu.html', {"menu": main_data})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes=[IsAuthenticated]

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
