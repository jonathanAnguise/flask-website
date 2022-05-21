import flask
from flask import Flask, render_template
from requests import get

SUPPORTED_LANGUAGES = ["en", "fr", "es"]
GITHUB_API = "https://api.github.com/users/jonathanAnguise/repos"
MY_GITHUB_URL = "https://github.com/jonathanAnguise"

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
    my_projects = get_projects_from_github()
    try:
        return render_template("personal_proj.html",
                           language=default_language,
                           my_projects=my_projects,
                           len_my_project=len(my_projects)
                           )
    except:
        return flask.redirect(MY_GITHUB_URL)

def get_projects_from_github():
    return get(GITHUB_API).json()

if __name__ == '__main__':
    app.run(debug=True)
