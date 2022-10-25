from flask import Blueprint, render_template, request
import logging
import functions

POST_PATH = "posts.json"

# Create new blueprint 'main'
main = Blueprint('main', __name__)

# Initial Logging
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger_search = logging.getLogger('search')


@main.route('/')
def main_page():
    return render_template('index.html')


@main.route('/search')
def search_page():
    str_ = request.args.get('s')
    posts = functions.load_data_from_json(POST_PATH)
    if posts is None:
        return f'Bad file "{POST_PATH}"'
    try:
        subposts = functions.search_posts(str_, posts)
        rend = render_template('post_list.html', request=str_, posts=subposts)
    except Exception as e:
        logging.exception(f'Error search "{e}"')
        return f'Error search "{e}"'

    return rend
