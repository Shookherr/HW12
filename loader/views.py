from flask import Blueprint, render_template, request
import functions
import os

POST_PATH = "posts.json"

# Create new blueprint 'loader'
loader = Blueprint('loader', __name__)


@loader.route('/post')
def create_page():
    return render_template('post_form.html')


@loader.route('/post', methods=['POST'])
def upload_page():

    pict = request.files.get('picture')
    pict_path = functions.save_picture(pict)

    # Недопустимое расширение файла
    if pict_path is None:
        print(f'Unknown image file type ({pict_path})')

    text = request.form.get('content')
    functions.save_post({'pic': pict_path, 'content': text}, functions.load_data_from_json(POST_PATH), POST_PATH)

    return render_template('post_uploaded.html', pict=pict_path, text=text)

