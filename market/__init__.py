from datetime import datetime
from flask import Flask, redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from market.admin.views import OrderView, ProductView, MarketView
from market.models import db
from flask_admin.menu import MenuCategory, MenuLink, MenuView
from .models import Order, OrderProduct, Product

from flask_admin.menu import MenuCategory
from flask_admin import expose, AdminIndexView, BaseView


class HomePageView(AdminIndexView):
    @expose('/')
    def index(self):
        name = 'Mike1'
        return self.render('admin/main_page.html', name=name)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    admin = Admin(app, name='Online Market',
                  template_mode='bootstrap4', static_url_path='/static',
                  index_view=HomePageView(), endpoint='admin')

    admin.add_view(MarketView(name='Создать заказ', endpoint='/create_order'))
    admin.add_view(OrderView(Order, db.session, name='Все заказы'))

    admin.add_view(ProductView(Product, db.session, name='Продукты'))

    return app


app_ctx = create_app()
