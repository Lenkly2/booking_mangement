from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Room, RoomType, BookingRoom,Customer

# Create your views here.
def index(request):
    return render(request, "hotel_booking/index.html")

def room_list(request):
    data = Room.objects.all()
    print(data)
    return render(request, "hotel_booking/room_list.html", context={"list": data})

def booking_room_list(request):
    data = BookingRoom.objects.all()
    print(data)
    return render(request, "hotel_booking/room_list.html", context={"list": data})

def booking_form(request: HttpRequest):
    if request.method == "GET":
        return render(request, "hotel_booking/booking_form.html")
    elif request.method == "POST":
        form_data = request.POST
        cust_id = form_data.get("cust_id",None)
        room_id = form_data.get("room_id",None)
        datetime = form_data.get("datetime",None)

        return redirect(request.path_info)