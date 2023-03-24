import json
import uuid
from datetime import datetime
from http.client import BAD_REQUEST

from flask import abort, flash, redirect, render_template, request, url_for

from market import app_ctx
from market.forms import OrderForm, ProductForm
from market.models import Order, OrderProduct, Product, db
from market.utils import products


@app_ctx.route('/')
def index():
    return render_template('market/index.html')


@app_ctx.route('/order/<int:order_id>')
def order_details(order_id):
    order = Order.query.get_or_404(order_id)
    total_price = sum(
        [op.product.price * op.quantity for op in order.products])
    return render_template('market/order_details.html', order=order, total_price=total_price, order_id=order.id, user_name=order.user_name)
