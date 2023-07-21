from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")       
def hello_world():
    """Returns the home page"""
    return render_template("index.html")


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()