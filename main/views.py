from flask import Blueprint, render_template, request
import functions

POST_PATH = "posts.json"

# Create new blueprint 'main'
main = Blueprint('main', __name__)


@main.route('/')
def main_page():
    return render_template('index.html')


@main.route('/search')
def search_page():
    str_ = request.args.get('s')
    return render_template('post_list.html', request=str_,
                           posts=functions.search_posts(str_, functions.load_data_from_json(POST_PATH)))
