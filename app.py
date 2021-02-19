from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/classes/')
def about():
    return render_template('classes.html')


if __name__ == '__main__':
    app.run()
