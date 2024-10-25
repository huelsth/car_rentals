# rentals/views.py

from django.shortcuts import render, get_object_or_404
from .models import CarModel, Booking, Driver, Extra
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

def car_list(request):
    cars = CarModel.objects.all()
    return render(request, 'rentals/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(CarModel, pk=car_id)
    extras = Extra.objects.all()
    drivers = Driver.objects.all()
    if request.method == 'POST':
        driver = get_object_or_404(Driver, pk=request.POST['driver_id'])
        start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
        selected_extras = request.POST.getlist('extras')
        payment_method = request.POST['payment_method']

        # Calculate total price
        total_days = (end_date - start_date).days
        total_price = car.price_per_day * total_days
        for extra_id in selected_extras:
            extra = get_object_or_404(Extra, pk=extra_id)
            total_price += extra.price * total_days

        booking = Booking.objects.create(
            car_model=car,
            driver=driver,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            payment_method=payment_method
        )
        booking.extras.set(selected_extras)
        return HttpResponseRedirect(reverse('booking_confirmation', args=[booking.id]))

    return render(request, 'rentals/car_detail.html', {'car': car, 'extras': extras, 'drivers': drivers})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'rentals/booking_confirmation.html', {'booking': booking})

#final version
