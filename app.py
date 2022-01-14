import os.path

from flask import Flask, render_template, abort

app = Flask(__name__, static_url_path="/static", static_folder="static")


@app.route('/')
def hello_world():
    if os.path.isdir("./static/empty_folder"):
        return render_template("base.html")
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
