# rentals/admin.py

from django.contrib import admin
from .models import CarModel, Extra, Driver, Booking

admin.site.register(CarModel)
admin.site.register(Extra)
admin.site.register(Driver)
admin.site.register(Booking)
