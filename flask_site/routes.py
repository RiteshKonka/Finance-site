from flask import render_template, url_for
from flask_site import app

@app.route('/')
# @app.route('/home')
def home():
    return render_template('index.html')