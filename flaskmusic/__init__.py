from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOADED_AUDIOS_DEST'] = 'flaskmusic/static/music'
app.config['ALBUM_ART_DEST'] = 'flaskmusic/static/albumarts'

if not os.path.isdir(app.config['UPLOADED_AUDIOS_DEST']):
    os.mkdir(app.config['UPLOADED_AUDIOS_DEST'])

if not os.path.isdir(app.config['ALBUM_ART_DEST']):
    os.mkdir(app.config['ALBUM_ART_DEST'])

db = SQLAlchemy(app)

from flaskmusic.routes import *
