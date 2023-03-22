from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from market.models import Product, db
from wtforms import SubmitField, IntegerField, StringField, FormField, HiddenField
from wtforms import StringField, IntegerField, SubmitField, FloatField, FieldList
from wtforms.validators import DataRequired, NumberRange, Optional, InputRequired


class ProductForm(FlaskForm):
    product_id = HiddenField()
    name = StringField('Название товара', render_kw={'readonly': True})
    quantity = IntegerField('Количество', validators=[Optional()])
    price = FloatField('Цена', render_kw={'readonly': True})


class OrderForm(FlaskForm):
    user_name = StringField('Name', validators=[InputRequired()])
    products = StringField('Products', validators=[InputRequired()])
    quantities = StringField('Quantities', validators=[InputRequired()])
    submit = SubmitField('Place Order')









