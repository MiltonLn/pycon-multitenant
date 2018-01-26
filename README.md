# MULTITENANT ARCHITECTURES IN PYTHON
![Descriptive image](pycon_milton.jpg)

This is the repository for the Multitenant implementation shown in my talk at
[PyCon Colombia 2018](https://www.pycon.co/)

For this project we are using [django-tenant-schemas](https://django-tenant-schemas.readthedocs.io/en/latest/),
please check the documentation for a full scope of its features.

## General Description

This is a dummy project to show you how to implement a multitenant architecture
using a `single database, multiple schemas` model.

The project is a tiny notes creators in which you can create tenants and inside
each tenant you can create some notes and check how they are isolated per schema.

I've tried to document very well the code and also it has a clean Django implementation,
but, if for some reason you are having troubles with some section of the code
or I didn't make myself clear or even you want to discuss about multitenant in general,
don't hesitate to contact me and I'll be glad to help you!

## Contact me!
* Email: miltonln04@gmail.com
* Twitter: @MiltonLn

## Installation

* Clone the project: `git clone https://github.com/MiltonLn/pycon-multitenant.git`
* Create a virtualenv for the project, i.e: `virtualenv -p ``which python3.6`` venv`
* Activate your virtualenv and install requirements: `pip install -r requirements.txt`
* Create a postgres role and database for the project, the current values in the settings are
user, password, db: pycon_multitenant
* Migrate the database, **REMEMBER**, in `django-tenant-schemas` we should always 
use `migrate_schemas`, so: `python manage.py migrate_schemas`
* In `django-tenant-schemas` we always need to create a db record for the public
tenant, fortunately, I've created a handy django command to do this, so you can run:
`python manage.py create_public_tenant`, please don't hesitate to check its implementation
in `pycon_multitenant/tenants/management/commands/create_public_tenant`
* You are ready to go! just run: `python manage.py runserver` to test the project
and create some tenants
