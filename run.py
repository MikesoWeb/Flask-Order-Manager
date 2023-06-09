
from market.forms import OrderForm
from market.models import Product, db
from market.routes import index
from market.utils import add_products_to_db, products

if __name__ == '__main__':
    from market.app import app_ctx
    with app_ctx.app_context():
        db.create_all()
        add_products_to_db(products)
    app_ctx.run(debug=True)
