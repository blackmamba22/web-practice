from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pooch'
bootstrap = Bootstrap(app)

import views
