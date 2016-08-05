# Flask App with Security, RESTful, and SQLAlchemy Boilerplate

This boilerplate offers a quickstart for building a Python-Flask RESTful API, with built-in support for PostgreSQL, using SQLAlchemy as an ORM. It also makes use of Flask-Security in order to control Users and Roles, as well as Flask-Migrate, to manage database migrations.

This project template is very similar to the one written by **Leo-G**, found here: https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

## Overview

This project is a simple Dog-Owner tracker. The owners are considered Users, and we've set up Users, and roles (among other [things](https://pythonhosted.org/Flask-Security/features.html)) through ```Flask-Security```. The models (found in ```db > models.py```) are declared and managed using ```SQLAlchemy```. The ```Flask-Restful``` API can be seen throughout the project, though the ```dog.py``` and ```owner.py``` files in the ```resources``` directory will be of most use when figuring out how to set up the HTTP methods through class-based methods.

We're using ```Flask-JWT``` for authentication and authorization.

The configuration for ```Flask-migrate``` can be seen in the ```migrate.py``` file in the project root.

As in the [project](https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API) by **Leo-G**, we make use of ```marshmallow``` and ```marshmallow_jsonapi``` for JSON and data validation. Schemas are declared for every model in the ```models.py``` file, and validation is performed in the different resource files.

## Pip Packages Needed:

- flask
- flask-security
- flask-restful
- flask-cors
- flask-sqlalchemy
- flask-migrate
- flask-script
- flask-jwt
- marshmallow
- marshmallow_jsonapi
- pyscopg2

## Before Running Server - Set Up Database:

Create your DB in Postgres using the credentials stored in the ```config/base_settings.py``` file (see the ```setup.md``` file for instructions on doing this), and then run the following from the project root:

```bash
python3 migrate.py db init
python3 migrate.py db migrate
python3 migrate.py db upgrade
```

## JSON Request Format When No Authorization Needed

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

## Protected API Endpoints

As you can see in  the ```user.py``` file, all of the CRUD features for the ```User``` class are protected by the decorator ```jwt_required()```. This means that a valid Authorization token is needed in order to reach those endpoints and perform that logic. In order to get a valid auth token, send a POST request to this url: ```/api/v1/auth``` with the Content-Type Header of ```application/json```, passing in the following:

```
{
    "ownername": "EMAIL",
    "ownerpassword": "PASSWORD"
}
```

**Note**: Rather than the JWT standard of ```"username"``` and ```"password"``` as the authorization keys, we've specified different keys, really just to show that you can. These keys are declared in the respective config files.

Once you send that request, you should get the following back:

```
{
    "access_token": "AUTH_TOKEN"
}
```

Using this token, you can then call the protected endpoints by adding the following headers to your calls:

```
Authorization : JWT AUTH_TOKEN
```

**Note**: Again, you can change the "JWT" value in the Auth header in the config file. We just chose not to in order to not conflict with OAuth2 Bearer tokens (as per the JWT documentation).

## Users - Setup

You'll notice that there are several lines of code under the "Bootstrap Several Users" section in ```main.py```. These users will be created if there are no users in the database, once you run the server, and hit an endpoint. I recommend using [Postman](https://www.getpostman.com/) to hit the endpoint ```localhost:5000/api/v1/dogs``` to get these users started.

**Note:** Make sure that once you're aware of this code there and the users that they create if using this boilerplate for a production-level application!
