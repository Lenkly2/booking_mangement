from django.urls import path
from .views import index, room_list,booking_room_list,booking_form

urlpatterns = [
    path("", index),
    path("room_list/",room_list),
    path("booking_room_list/",booking_room_list),
    path("booking_form/",booking_form),
]
