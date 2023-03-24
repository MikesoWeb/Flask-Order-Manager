from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    initialized = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('OrderProduct', backref='order', lazy=True)
    



class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'))
    quantity = db.Column(db.Integer)
    product = db.relationship('Product', backref='order_products')
    def __repr__(self):
        return f'{self.product.name} ({self.quantity})'