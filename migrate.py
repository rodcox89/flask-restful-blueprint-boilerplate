############################################################################################
# Migrate script
#
# This file is necessary to initialize and keep track of database migrations.
############################################################################################
from main import app
from db.models import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
