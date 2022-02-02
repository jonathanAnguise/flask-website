from flask import Flask, render_template

SUPPORTED_LANGUAGES = ["en", "fr", "es"]

app = Flask(__name__)


@app.route('/<default_language>')
@app.route('/')
def hello(default_language='en'):
    if default_language not in SUPPORTED_LANGUAGES:
        not_existing = f'<p> Sorry the page "{default_language}" is not existing</p><br>\
        <iframe src="https://giphy.com/embed/dJYoOVAWf2QkU"\
         width="480" height="267" frameBorder="0" class="giphy" </iframe>'
        return not_existing
    return render_template("index.html", language=default_language)


@app.route('/<default_language>/personal_project')
def perso_proj(default_language='en'):
    return f"<h1>{default_language} -- Page to do</h1>"


if __name__ == '__main__':
    app.run(debug=True)
