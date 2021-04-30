from flask import render_template, url_for, flash, redirect, jsonify, request
from flaskmusic import app, db, bcrypt
from flaskmusic.forms import *
from flaskmusic.models import *
from werkzeug import secure_filename
from flaskmusic.utils import *
import os
import json
import secrets
from PIL import Image
from flask_login import login_user, current_user, logout_user, login_required
import random

@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route("/<user>", methods=['GET', 'POST'])
@login_required
def home(user):

    if not os.path.isdir(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user)):
        os.mkdir(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user))
    if not os.path.isdir(os.path.join(app.config['ALBUM_ART_DEST'], user)):
        os.mkdir(os.path.join(app.config['ALBUM_ART_DEST'], user))

    metadata = []
    songs = os.listdir(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user))
    for song in songs:
        a = get_meta(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user),
                     os.path.join(app.config['ALBUM_ART_DEST'], user), song)
        # print(a)
        metadata.append(a)

    form = MusicForm()

    if form.validate_on_submit():
        for file in form.music.data:
            file_filename = secure_filename(file.filename)
            ext = file.filename.split('.')[-1]
            if ext in ("mp3", "m4a", "aac"):
                file.save(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], f'{user}/{file_filename}'))
                flash('Uploaded Sucessfully', 'success')
                return redirect(url_for('home', user=user, form=form, songs=metadata))
            else:
                flash('Only audios allowed', 'danger')
                return redirect(url_for('home', user=user, form=form, songs=metadata))

    return render_template('player.html', form=form, songs=metadata, user=user)


# @app.route("/lyrics", methods=['GET', 'POST'])
# def return_lyrics():
#     if request.method == 'POST':
#         data = request.get_json()
#         lyrics = get_lyrics_musixmatch(
#             q_artist=data['artist'], q_track=data['song'])
#         return jsonify({"lyrics": lyrics})
#     return jsonify({"status_code": "ok"})


@app.route("/delete/<user>/<song>")
def deletesong(user, song):
    os.remove(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], f'{user}/{song}'))
    form = MusicForm()
    metadata = []
    songs = os.listdir(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user))
    for song in songs:
        a = get_meta(os.path.join(app.config['UPLOADED_AUDIOS_DEST'], user),
                     os.path.join(app.config['ALBUM_ART_DEST'], user), song)
        metadata.append(a)
    return redirect(url_for('home', user=user, form=form, songs=metadata))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)
