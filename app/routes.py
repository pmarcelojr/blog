from flask import render_template
from app import app

@app.route('/')
@app.route('/index/')
def index():
    user = {'username': 'Marcelo'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Iniciando meu Projeto'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Voce consegue'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
