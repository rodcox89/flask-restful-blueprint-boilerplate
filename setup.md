# Initial DB Setup

Before you use the ```migrate.py``` functionality, you will need to set up the PostgreSQL database.

## Create PostgreSQL User
```bash
# Create correct user for this project
createuser -d -l -P dog_dev
```

### Flags Explained

- -d: Allows user to create databases
- -l: Allows user to login
- -P: Requires prompt to set up password for the user

## Create Database

Run this from the terminal, not from the ```psql``` prompt:

```bash
createdb -O dog_dev -U dog_dev dog_dev_db
```

### Flags Explained

- -O: User that will own the database
- -U: User to log in as in order to create the database

## Misc

In the process of setting up an application, testing models, and moving forward, you might run into the need to do some more in the PSQL. Here are a couple of other references for dealing with PostgreSQL.

### Drop Database

Run this command from your terminal, not the ```psql``` prompt:

```bash
dropdb -U dog_dev dog_dev_db
```
