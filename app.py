from flask import Flask, send_from_directory

# Blueprints import
from main.views import main
from loader.views import loader

app = Flask(__name__)


@app.route('/uploads/images/<path:path>')
def static_dir(path):
    return send_from_directory('uploads/images', path)


# Blueprints register
app.register_blueprint(main)
app.register_blueprint(loader)

app.run()
