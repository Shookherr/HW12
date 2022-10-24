from flask import Blueprint, render_template

# Create new blueprint 'main'
main = Blueprint('main', __name__)


@main.route('/photo')
def main_page():
    pass
    # return render_template('index.html')
