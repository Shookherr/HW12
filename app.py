from flask import Flask, render_template, request, send_from_directory
import functions
# Blueprints import
from main.views import main

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Считать все
all_posts = functions.load_data_from_json(POST_PATH)

# Blueprints register
app.register_blueprint(main)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/post_list.html?s=<s>')
def page_tags():
    # s = request.args.get('s')
    # return render_template('post_list.html', request=s, posts=all_posts)

# @app.route('/search')
# def page_search():
#     s = request.args.get('s')
#     return render_template('post_list.html', request=s, posts=all_posts)
    return render_template('post_list.html', request='кит', posts=all_posts)


# @app.route("/list")
# def page_tag():
#     pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
