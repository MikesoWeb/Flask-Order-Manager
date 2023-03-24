from datetime import datetime
from flask import redirect, render_template, request, url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuCategory, MenuLink
from markupsafe import Markup
from flask_admin import expose, AdminIndexView, BaseView
from market.models import Order, OrderProduct, Product
from market.models import db


class MarketView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def main(self):
        if request.method == 'POST':
            data = request.get_json()
            user_name = data['user_name']
            products = data['products']
            quantities = data['quantities']
            order = Order(user_name=user_name, created_at=datetime.now())
            db.session.add(order)
            db.session.commit()

            for i in range(len(products)):
                if products[i] and quantities[i] and int(quantities[i]) > 0:
                    product = Product.query.get(products[i])
                    quantity = quantities[i]
                    order_product = OrderProduct(
                        order=order, product_id=product.id, quantity=quantity)
                    db.session.add(order_product)

            db.session.commit()
            return redirect(url_for('order_details', order_id=order.id))

        products = Product.query.all()

        return self.render('admin/market_list.html', products=products)

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
