# populate_database.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental.settings')
django.setup()

from rentals.models import CarModel, Extra, Driver

def create_car_models():
    CarModel.objects.create(name='Toyota Camry', price_per_day=50, price_per_week=300, available=True)
    CarModel.objects.create(name='Honda Civic', price_per_day=40, price_per_week=250, available=True)
    CarModel.objects.create(name='Ford Mustang', price_per_day=70, price_per_week=400, available=True)

def create_extras():
    Extra.objects.create(name='Navigation', price=10)
    Extra.objects.create(name='Insurance', price=20)
    Extra.objects.create(name='Extra Driver', price=15)

def create_drivers():
    Driver.objects.create(name='John Doe', license_number='ABC123', id_card_number='12345', email='john@example.com')
    Driver.objects.create(name='Jane Smith', license_number='XYZ789', id_card_number='67890', email='jane@example.com')

if __name__ == '__main__':
    create_car_models()
    create_extras()
    create_drivers()
    print("Database populated successfully.")
