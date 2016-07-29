# Flask App with Security, RESTful, and SQLAlchemy Boilerplate

This boilerplate offers a quickstart for building a Python-Flask RESTful API, with built-in support for PostgreSQL, using SQLAlchemy as an ORM. It also makes use of Flask-Security in order to control Users and Roles, as well as Flask-Migrate, to manage database migrations.

This project template is very similar to the one written by **Leo-G**, found here: https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

## Pip Packages Needed:

- flask
- flask-security
- flask-restful
- flask-cors
- flask-sqlalchemy
- flask-migrate
- flask-script
- marshmallow
- marshmallow_jsonapi
- pyscopg2

## Before Running Server:

Create your DB in Postgres using the credentials stored in the ```db/base_settings.py``` file, and then run the following from the project root:

```bash
python3 migrate.py db init
python3 migrate.py db migrate
python3 migrate.py db upgrade
```

## JSON Request Format

When sending a POST request in order to create a new object (in this case, a Dog), you will need to follow a very strict format, or the JSON validator will reject it. This format is the following:

```
{
    "data": {
        "type": "dog",
        "attributes": {
            "dog_type": "INSERT DOG TYPE HERE"
        }
    }
}
```

**Note**: If make sure the value for the "type" key matches the "type" value in the ```Meta``` class of whatever ```Schema``` used to validate your object. You also can input however many attributes for your object as you'd like in the "attributes" dictionary.
