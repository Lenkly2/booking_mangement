from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=13)

class RoomType(models.Model):
    type_choices = {
        "cheap": "Econom-class",
        "mid": "middle-class",
        "reach": "Business-class"
    }

    type = models.CharField(max_length=20, choices=type_choices)

class Room(models.Model):
    type_id = models.ForeignKey(RoomType, on_delete=models.SET_NULL,null=True)
    


class BookingRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_user = models.ForeignKey(Customer,on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()