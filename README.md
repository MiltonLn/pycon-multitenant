# MULTITENANT ARQUITECTURES IN PYTHON BY MILTON LENIS
Multitenant example project using django-tenant-schemas
gi
![Descriptive image](pycon_milton.jpg)

## Installation

* Clone the project: `git clone https://github.com/MiltonLn/pycon-multitenant.git`
* Create a virtualenv for the project, i.e: `virtualenv -p `which python3.6` venv`
* Activate your virtualenv and install requirements: `pip install -r requirements.txt`
* Create a postgres role and database for the project, the current values in the settings are
user, password, db: pycon_multitenant
* Migrate the database, **REMEMBER**, in `django-tenant-schemas` we should use 
always `migrate_schemas`, so: `python manage.py migrate_schemas`
* In `django-tenant-schemas` we always need to create a db record for the public
tenant, fortunately, I've created a handy django command to do this, so you can run:
`python manage.py create_public_tenant`, please don't hesitate to check its implementation
in `pycon_multitenant/tenants/management/commands/create_public_tenant`
* You are ready to go! just run: `python manage.py runserver` to test the project
and create some tenants
