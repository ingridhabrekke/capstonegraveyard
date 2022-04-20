from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from datetime import datetime
import os

app = Flask(__name__)

# bundle CSS
css = Bundle('src/style.css', output='css/main.css', filters='postcss')

assets = Environment(app)
assets.register('main_css', css)
css.build()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse')
def users():
    return render_template('browse.html', users=users)

@app.route('/add')
def login():
    return render_template('add.html')

if __name__ == '__main__':
    app.run()
