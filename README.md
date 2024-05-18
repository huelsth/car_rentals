# Django Car Rental Project

This is a Django project for a car rental application. The project allows users to browse available cars, view car details, book cars, and manage bookings.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtualenv (recommended)



## sh
git clone https://github.com/yourusername/car_rental.git
cd car_rental
this project is public

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt



SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3


##apply database migration

python manage.py makemigrations
python manage.py migrate


## create superuser

python manage.py createsuperuser


## collect static file

python manage.py collectstatic

##run server 

python manage.py runserver


## project structure 

car_rental/
    manage.py
    car_rental/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    rentals/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        tests.py
        urls.py
        views.py
        templates/
            rentals/
                car_list.html
                car_detail.html
                booking_confirmation.html
        
    requirements.txt
    README.md
