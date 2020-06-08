# -*- coding:utf-8 -*-
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app import db
from config.config import configs


app = create_app(configs['ENV'])
manager = Manager(app)
migrate = Migrate(app, db)


# def make_shell_context():
#     return dict(app=app, db=db, models=models)
# 
# 
# manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
