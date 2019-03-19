# IWS Feature Requests application

A web application built with Flask

## Tools Used

Below are the tools used for this project.

* Python 3.6.4
* Flask - the main web framework
* SqlAlchemy as an ORM for database operations
* MySQL - the main database
* Flask-Migrate for handling database migrations
* WTForms for form validation
* Jinja2 for templates
* gunicorn for serving
* Cleave.js for "cleaving" date
* Spectre minimalistic css framework
* Fabric3 for application deployment
* Also, some other interesting libraries for the proper engineering of the above


## Project Description


This is a web application that allows requests for a new software feature that will be added onto an existing piece of software to be created and submitted - as tickets.

This application uses three main models:

* `Request`: This is the main model that the application is about. It
  contains the fields `id` (primary key), `title`, `description` (text field), `client_id`
  (foreign key to Client model),
  `priority` (integer field, will be unique for each client's feature
  requests), `target_date` (the desired date for this feature request) and 
  `product` (foreign key to the `ProductEnum` model)
* `Client`: This is a simple model with a name that will be used to persist the
  clients that require the features
* `ProductEnum`: Another simple model similar to Client, will persist the product
  areas of each feature request.


## Project Structure

This is a rather simple project. It has just one package (`request`) that
contains everything:

* The `__init__.py` file contains the Flask app and database initialization.
* The `forms.py` has the definition of the Request form
* The `models.py` contains the ORM definition of the database tables
* The `routes.py` contains the definition of the various views that are used

There's also a template directory with the jinja2 templates and a static
directory with a bunch of css and js files.


## How to build and deploy the project

```
Set Up a Virtual Environment
```
`pip3.6 install virtualenv`

`virtualenv chosenname`

`source ./chosenname/bin/activate`

```
install requirements
```
`pip3.6 install -r requirements.txt`

```
Delete 'app.db in ./config folder, and delete entire ./migrations folder'
```

If you would like to use Sqlite3 for development,
add something like

``` python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')
```

If you want to use mysql: 

``` python
SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:pass@host/database'
```

`export FLASK_APP=request.py`

Create a new database, migrate and update the changes to your database with these commands below

`flask db init`
`flask db migrate`
`flask db upgrade`


Create 3 or more client objects

create sample client objects from your python shell, using the syntax below while creating the objects.

This should come in handy: http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

``` bash
client1 = Client(name='Client A')
.
.
.
client5 = Client(name='Client E')
```

```
then create requests for each clients from the main interface
```
Finally, you can run the server by running 

`flask run`


## Testing

The folder `tests` contains a file `test_views.py` which contains proper tests for all the views of the application. 
To run tests, just run the command below at the application root.

`pytest`

## Demo

<http://iws-britecore.herokuapp.com/>
# iws-feature-request
