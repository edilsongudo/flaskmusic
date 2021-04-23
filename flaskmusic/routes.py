from flask import render_template, url_for, flash, redirect
from flaskmusic import app
from flaskmusic.forms import MusicForm
from flask import request
from werkzeug import secure_filename
from flask_uploads import configure_uploads, AUDIO, UploadSet
import os
import eyed3
import json


def returntags(file):
    audio_file = eyed3.load(file)
    album_name = audio_file.tag.album
    artist_name = audio_file.tag.artist
    return {'file': file, 'album_name': album_name, 'artist_name': artist_name}


audios = UploadSet('audios', ("mp3", "m4a", "aac"))
configure_uploads(app, audios)


@app.route("/", methods=['GET', 'POST'])
def home():

    songs = os.listdir(app.config['UPLOADED_AUDIOS_DEST'])

    # songs_meta = []
    # for file in os.listdir(app.config['UPLOADED_AUDIOS_DEST']):
    #     songs_meta.append(returntags(os.path.join(
    #         app.config['UPLOADED_AUDIOS_DEST'], file)))

    # for i in range(len(songs_meta)):
    #     songs_meta[i]['file'] = songs[i]
    #     print(songs_meta[i]['file'])

    form = MusicForm()
    if form.validate_on_submit():
        try:
            for file in form.music.data:
                file_filename = secure_filename(file.filename)
                audios.save(file)
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_filename))
            flash('Uploaded Sucessfully', 'success')
            return redirect('/')
        except:
            flash('Only audios allowed', 'danger')
            return redirect('/')
    return render_template('home.html', form=form, songs=songs)


@app.route("/player/")
def player_with_no_last():
    songs = os.listdir(app.config['UPLOADED_AUDIOS_DEST'])
    return render_template('player.html', songs=json.dumps(songs), last=json.dumps({'last': 'return -1'}))


@app.route('/player/<last>')
def player(last):
    songs = os.listdir(app.config['UPLOADED_AUDIOS_DEST'])

    return render_template('player.html', songs=json.dumps(songs), last=json.dumps(last))
