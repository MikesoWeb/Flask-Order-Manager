from flask import Flask, flash, render_template, redirect, url_for
from market.models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    return app

app_ctx = create_app()



