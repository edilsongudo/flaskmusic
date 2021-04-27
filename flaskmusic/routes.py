from flask import render_template, url_for, flash, redirect, jsonify, request
from flaskmusic import app
from flaskmusic.forms import MusicForm
from werkzeug import secure_filename
from flask_uploads import configure_uploads, AUDIO, UploadSet
from flaskmusic.utils import get_meta, get_lyrics_musixmatch
import os
import json


audios = UploadSet('audios', ("mp3", "m4a", "aac"))
configure_uploads(app, audios)


@app.route("/", methods=['GET', 'POST'])
def home():
    metadata = []
    songs = os.listdir(app.config['UPLOADED_AUDIOS_DEST'])
    for song in songs:
        a = get_meta(app.config['UPLOADED_AUDIOS_DEST'],
                     app.config['ALBUM_ART_DEST'], song)
        # print(a)
        metadata.append(a)

    form = MusicForm()
    if form.validate_on_submit():
        try:
            for file in form.music.data:
                file_filename = secure_filename(file.filename)
                audios.save(file)
            flash('Uploaded Sucessfully', 'success')
            return redirect('/')
        except:
            flash('Only audios allowed', 'danger')
            return redirect('/')
    return render_template('home.html', form=form, songs=metadata)


@app.route("/lyrics", methods=['GET', 'POST'])
def return_lyrics():
    if request.method == 'POST':
        data = request.get_json()
        lyrics = get_lyrics_musixmatch(
            q_artist=data['artist'], q_track=data['song'])
        return jsonify({"lyrics": lyrics})
    return jsonify({"status_code": "ok"})
