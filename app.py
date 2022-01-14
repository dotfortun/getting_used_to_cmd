from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def hello_world():
    return render_template("base.html")


if __name__ == '__main__':
    app.run()
