
Name:
-----
PRODUCT MANAGEMENT API


Description:
------------
This is the API based on Django REST_FRAMEWORK which will communicate to Django Product Management Application
and allow the authentic user to do some required operations like create,retrieve,update,delete.
In this application Sqlite database is used.


Installation:
------------
The following python packages are required to be installed for the application, by using pip command.
>pip install (package name)

packages
--------
> Django==3.2.9
> djangorestframework==3.12.4
> virtualenv==20.10.0
> requests == 2.26.0
> flake8 == 3.9.2
> black == 21.11b1

The requirements.txt file in the repository lists the Python package dependencies.

Configuration:
---------------

In settings.py file of the API application it requires to add the "rest_framework" application
in INSTALLED_APP section to use the libraries of rest_framework app.

once configuration and installation will complete,the migrations should be applied to build the database structure
> python manage.py makemigrations
> python manage.py migrate

finally, it requires to runserver with port number 0909.
> python manage.py runserver.

Usage
------

> Auth Token is not used in this application, we can use this concept to make our application more secure.


