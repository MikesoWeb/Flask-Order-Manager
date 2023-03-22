from datetime import datetime
from http.client import BAD_REQUEST
import uuid
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    initialized = db.Column(db.Boolean, default=False, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('OrderProduct', backref='order', lazy=True)

class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer)
    product = db.relationship('Product', backref='order_products')

