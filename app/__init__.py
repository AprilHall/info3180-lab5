from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

from app import views