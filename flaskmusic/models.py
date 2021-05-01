from datetime import datetime
from flaskmusic import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.String(20), nullable=True)
    songs = db.relationship('Song', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_filename = db.Column(db.String(120), nullable=False)
    song_title = db.Column(db.String(120), nullable=True)
    song_author = db.Column(db.String(120), nullable=True)  # delete
    song_artist = db.Column(db.String(120), nullable=True)
    song_genre = db.Column(db.String(60), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Song('{self.song_filename}', '{self.date_posted}')"
