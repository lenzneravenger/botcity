import os
import os.path

files = os.listdir('./files')
botcity = ["images", "media", "word documents", "pdfs"]

for i in botcity:
    if not os.path.exists(f'./files/{i}'):
        os.mkdir(f'./files/{i}')

for current_file in files:
    extended_file = f'files/{current_file}'
    if os.path.splitext(current_file)[1]=='.png' or  os.path.splitext(current_file)[1]=='.jpeg':
        os.rename(os.path.abspath(extended_file), os.path.abspath(f'./files/images/{current_file}'))

    if os.path.splitext(current_file)[1]=='.mp4':
        os.rename(os.path.abspath(extended_file), os.path.abspath(f'./files/media/{current_file}'))

    if os.path.splitext(current_file)[1]=='.docx':
        os.rename(os.path.abspath(extended_file), os.path.abspath(f'./files/word documents/{current_file}'))

    if os.path.splitext(current_file)[1]=='.pdf':
        os.rename(os.path.abspath(extended_file), os.path.abspath(f'./files/pdfs/{current_file}'))

