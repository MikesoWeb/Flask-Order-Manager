from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (FieldList, FloatField, FormField, HiddenField,
                     IntegerField, StringField, SubmitField)
from wtforms.validators import (DataRequired, InputRequired, NumberRange,
                                Optional)

from market.models import Product, db


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
