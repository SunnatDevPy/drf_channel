mig:
	python manage.py makemigrations
	python manage.py migrate

user:
	python manage.py createsuperuser

run:
	python manage.py runserver
