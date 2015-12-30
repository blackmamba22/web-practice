from flask.ext.script import Shell, Manager
from app import app, db, models

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=models.User, Role=models.Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.run()
