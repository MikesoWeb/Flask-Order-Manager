from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from market.admin.views import HomeLink, OrderView, ProductView
from market.models import db

from .models import Order, Product


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    admin = Admin(app, name='Online Market',
                  template_mode='bootstrap3', static_url_path='/static')

    admin.add_link(HomeLink(name='Главная', url='/',
                   endpoint='index', target='_blank'))
    admin.add_view(ProductView(Product, db.session, name='Продукты'))
    admin.add_view(OrderView(Order, db.session, name='Заказы'))

    return app


app_ctx = create_app()
