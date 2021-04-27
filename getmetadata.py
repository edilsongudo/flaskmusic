# import music_tag
# from PIL import Image
# import io
# import os

# # img = Image.open(io.BytesIO(image_data))
# # img.show()


# def get_meta(folder, file):

#     song = os.path.join(folder, file)
#     meta = music_tag.load_file(song)

#     try:
#         image_data = meta['artwork'].first.data
#         filename = file.split('.')[0] + '.jpg'
#         with open(os.path.join(f'{folder}/album', filename), 'wb') as file:
#             file.write(image_data)
#     except Exception as e:
#         print(e)

#     return {'album': meta['album']., 'artist': meta['artist'], 'title': meta['tracktitle'], 'filename': file}


# a, b = 'flaskmusic/static/music', 'Shakka_-_When_Will_I_See_You_Again_AMTRAC_Remix.m4a'
# get_meta(a, b)
