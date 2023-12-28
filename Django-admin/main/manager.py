from main import db, main
from flask_migrate import Migrate

migrate = Migrate(main, db)

if __name__ == '__main__':
    main.run()