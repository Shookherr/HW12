from flask import Blueprint, render_template, request
import logging
import functions

POST_PATH = "posts.json"

# Create new blueprint 'loader'
loader = Blueprint('loader', __name__)

# Initial Logging
logging.basicConfig(filename='log.txt')
logger_bad_ext = logging.getLogger('bad_ext')


@loader.route('/post', methods=['GET'])
def create_page():
    return render_template('post_form.html')


@loader.route('/post', methods=['POST'])
def upload_page():

    pict = request.files.get('picture')
    pict_path = functions.save_picture(pict)

    # Недопустимое расширение файла
    if pict_path is None:
        logger_bad_ext.info('Unknown image file type')
        return 'Unknown image file type'

    text = request.form.get('content')

    posts = functions.load_data_from_json(POST_PATH)
    if posts is None:
        return f'Bad file "{POST_PATH}"'

    functions.save_post({'pic': pict_path, 'content': text}, posts, POST_PATH)
    return render_template('post_uploaded.html', pict=pict_path, text=text)
