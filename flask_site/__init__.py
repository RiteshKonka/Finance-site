from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hgWzZKbS0k8ewWE'

from flask_site import routes