from tinytag import TinyTag
import os


def get_meta(folder, file):
    song = os.path.join(folder, file)
    tag = TinyTag.get(song)
    return {'album': tag.album, 'artist': tag.artist, 'title': tag.title, 'filename': file}

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
