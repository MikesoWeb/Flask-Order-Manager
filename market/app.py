from flask import Flask
from flask_admin import Admin, AdminIndexView, expose
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from market.admin.views import MarketView, OrderView, ProductView
from market.models import Order, Product, User, db


class HomePageView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/main_page.html')


def create_admin_user():
    user = User(email='admin@example.com')
    user.password = 'qwerty'
    db.session.add(user)
    db.session.commit()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email='admin@example.com').first():
            create_admin_user()
    login_manager.login_view = 'index'
    login_manager.init_app(app)
    admin = Admin(app, name='Online Market',
                  template_mode='bootstrap4', static_url_path='/static',
                  index_view=HomePageView(), endpoint='admin')

    admin.add_view(MarketView(name='Создать заказ', endpoint='/create_order'))
    admin.add_view(OrderView(Order, db.session, name='Все заказы'))
    admin.add_view(ProductView(Product, db.session, name='Продукты'))

    # move the imports inside the function
    from market.routes import LoginView, LogoutView

    # admin.add_view(LoginView(name='Войти', endpoint='login'))
    admin.add_view(LogoutView(name='Выйти', endpoint='logout'))

    return app


app_ctx = create_app()
