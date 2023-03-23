from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from markupsafe import Markup

from market.models import Order, Product


class HomeLink(MenuLink):
    def get_url(self):
        return url_for('index')




class ProductView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    create_modal = True
    edit_modal = True
    delete_modal = True

    column_default_sort = ('name', True)
    column_searchable_list = ['name']

    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'name': 'Наименование',
        'price': 'Цена',
        'initialized': 'Иннициализирован',

    }


class OrderView(ModelView):

    can_create = False
    can_edit = True
    can_delete = True
    column_list = ('order_link', 'user_name', 'created_at', 'products')
    column_labels = {
        'user_name': 'Имя пользователя',
        'created_at': 'Дата создания',
        'products': 'Список продуктов',
        'order_link': 'Номер заказа'
    }

    def get_context(self):
        context = super(OrderView, self).get_context()
        context['orders'] = Order.query.all()
        return context

    def order_link_formatter(self, context, model, name):
        link = url_for('order_details', order_id=model.id, _external=True)
        return Markup(f'<a href="{link}" class="order-link">Заказ № {model.id}</a>')


    column_formatters = {
        'order_link': order_link_formatter
    }
