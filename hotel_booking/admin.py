from django.contrib import admin
from .models import BookingRoom,Room,RoomType,Customer
# Register your models here.

admin.site.register(BookingRoom)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Customer)

