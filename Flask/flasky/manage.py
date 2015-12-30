from flask.ext.script import Shell, Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db, models

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=models.User, Role=models.Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.run()
