import requests
from musixmatch import Musixmatch
# from tinytag import TinyTag
import os
import music_tag


def return_secret():
    with open('secret.scrt', 'r') as f:
        musixmatch_api_key = f.read().strip()
        return musixmatch_api_key


def get_meta(folder, album_dest, file):

    song = os.path.join(f'{folder}/{file}')
    meta = music_tag.load_file(song)

    try:
        image_data = meta['artwork'].first.data
        filename = file.split('.')[0] + '.jpg'
        with open(f'{album_dest}/{filename}', 'wb') as f:
            f.write(image_data)
    except Exception as e:
        print(e)

    return {'album': meta['album'].value, 'artist': meta['artist'].value, 'title': meta['tracktitle'].value, 'filename': file}


def get_meta_old(folder, file):
    song = os.path.join(folder, file)
    tag = TinyTag.get(song)
    print(tag)
    return {'album': tag.album, 'artist': tag.artist, 'title': tag.title, 'filename': file}


def get_lyrics():
    artist = input('Type the artist: ')
    title = input('Type the title: ')
    r = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
    return r.json()


def get_lyrics_musixmatch(api_key=return_secret(), q_artist='neovaii', q_track='meaning'):
    musixmatch = Musixmatch(api_key)
    result = musixmatch.track_search(q_artist=q_artist, q_track=q_track,
                                     page_size=10, page=1, s_track_rating='desc')

    track_id = result['message']['body']['track_list'][0]['track']['track_id']

    lyrics = musixmatch.track_lyrics_get(
        track_id)['message']['body']['lyrics']['lyrics_body']

    lyrics = lyrics.replace('\n', '<br>')

    return lyrics


# import os
# from io import BytesIO
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3
# from PIL import Image

# song = '../flaskmusic/static/music/'
# track = MP3(song)
# tags = ID3(song)
# print(track.pprint())
# print('---------------------------')
# print(tags.pprint())

# pic = tags.get('APIC:').data
# im = Image.open(BytesIO(pic))
# im.show()

# import audio_metadata
# metadata = audio_metadata.load(
#     '../flaskmusic/static/music/Nightcore_-_Easily_-_Lyrics128k.mp3')
# print(metadata)
