import json
import uuid
from datetime import datetime
from http.client import BAD_REQUEST

from flask import abort, flash, redirect, render_template, request, url_for

from market import app_ctx
from market.forms import OrderForm, ProductForm
from market.models import Order, OrderProduct, Product, db
from market.utils import products


@app_ctx.route('/', methods=['GET', 'POST'])
def index():
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

    return render_template('market/index.html', products=products)


@app_ctx.route('/order/<int:order_id>')
def order_details(order_id):
    order = Order.query.get_or_404(order_id)
    total_price = sum(
        [op.product.price * op.quantity for op in order.products])
    return render_template('market/order_details.html', order=order, total_price=total_price, order_id=order.id, user_name=order.user_name)
