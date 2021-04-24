from flask import render_template, url_for, flash, redirect
from flaskmusic import app
from flaskmusic.forms import MusicForm
from flask import request
from werkzeug import secure_filename
from flask_uploads import configure_uploads, AUDIO, UploadSet
from flaskmusic.utils import get_meta
import os
import json


audios = UploadSet('audios', ("mp3", "m4a", "aac"))
configure_uploads(app, audios)


@app.route("/", methods=['GET', 'POST'])
def home():
    meta = []
    songs = os.listdir(app.config['UPLOADED_AUDIOS_DEST'])
    for song in songs:
        meta.append(
            get_meta(folder=app.config['UPLOADED_AUDIOS_DEST'], file=song))

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
    return render_template('home.html', form=form, songs=meta)
