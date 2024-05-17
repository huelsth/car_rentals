# rentals/models.py

from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Extra(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    id_card_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    extras = models.ManyToManyField(Extra)
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'{self.car_model.name} booking by {self.driver.name}'
