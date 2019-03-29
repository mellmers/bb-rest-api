# BattleBulls RestAPI
Beautiful RESTApi built with Django REST framework for our website [battleground-bulls.de](https://battleground-bulls.de).

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

[See deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites
Things you need to install and run the software:

* Git
* Python/Pip
* MySql/Apache

## Installing
* Clone this repository
* `pip install -r requirements.txt`
* Create database and db user (details in [settings](battlebulls/settings.py))
* Run the server

## Run the software
For starting the server you have to execute the following command from the root directory :
```
python manage.py runserver <127.0.0.1:9000>
```
If you would to apply model changes, you need to run
```
python manage.py makemigrations
```
and
```
python manage.py migrate
```

## Documentation
If you started the server, you can find the swagger documentation under the URL `/docs/`

## Deployment
**TODO**: Add additional notes about how to deploy this on a live system.

## Built With:
* [Django REST framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Django REST Swagger](https://django-rest-swagger.readthedocs.io) - Swagger/OpenAPI Documentation Generator for Django REST Framework

## Authors
Moritz Ellmers - Initial work - [moritzellmers.de](https://moritzellmers.de)

See also the list of contributors who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
