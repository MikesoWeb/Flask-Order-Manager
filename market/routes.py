from market.models import User

from flask_login import current_user, login_user
from flask import Flask, redirect, render_template, url_for
from http.client import BAD_REQUEST
from urllib.parse import urlparse

from flask import abort, flash, redirect, render_template, request, url_for
from flask_admin import BaseView, expose
from flask_login import login_required, login_user, logout_user


from market.forms import LoginForm
from market.models import Order, OrderProduct, Product, User, db


class LoginView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(user.password, password):
                login_user(user)
                return redirect(url_for('admin.index'))
            else:
                flash('Неверные email или пароль', 'error')
        return self.render('market/index.html')


class LogoutView(BaseView):
    @expose('/')
    @login_required
    def index(self):
        logout_user()
        return redirect(url_for('index'))
    
    def get_context(self):
        context = super().get_context()
        context['admin_base_template'] = 'admin/master.html'
        return context

from market.app import app_ctx
@app_ctx.route('/', methods=['GET', 'POST'])
def index():
    
    form = LoginForm()
    if form.validate_on_submit():
        # Получаем пользователя с введенным email
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            # Если пользователь не найден или пароль не совпадает
            flash('Неверный email или пароль', 'danger')
            return redirect(url_for('index'))
        # Авторизуем пользователя
        login_user(user, remember=form.remember_me.data)
        # Переходим на следующую страницу (если она была указана в параметрах GET-запроса)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('admin.index')
        return redirect(next_page)
    return render_template('market/index.html', form=form)


@app_ctx.route('/order/<int:order_id>')
def order_details(order_id):
    order = Order.query.get_or_404(order_id)
    total_price = sum(
        [op.product.price * op.quantity for op in order.products])
    return render_template('market/order_details.html', order=order, total_price=total_price, order_id=order.id, user_name=order.user_name)
