from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '333'

from app import routes
