from flask_migrate import Migrate, MigrateCommand
from main import app, db
from flask_script import Manager

migrate = Migrate(app, db)

Manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    Manager.run()