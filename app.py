from market import app_ctx
from market.forms import OrderForm
from market.models import Product, db


product_names = ['Горбуша', 'Икра из кабачков', 'Кальмар натуральный', 'Камбала натуральная', 'Кета', 'Кижуч', 'Килька Крымская', 'Килька с овощами по-венгерски', 'Килька с овощами по-гавайски', 'Килька с овощами по-мексикански', 'Кукуруза глобал',  'Лосось', 'Масло подс.', 'Молоко сгущ.', 'Мясо цыплёнка', 'Наггетсы', 'Нерка', 'Печень и икра минтая натуральная', 'Печень минтая приморская', 'Сайра', 'Салат из морской капусты', 'Сардина атлантическая', 'Сардина в масле', 'Сельдь натуральная', 'Семга', 'Скумбрия натуральная', 'Томатная паста Иран 850', 'Томаты в банках', 'Тушенка говядина', 'Тушенка свинина', 'Тушеное мясо цыпленка', 'Фасоль бел.', 'Фасоль белая', 'Фасоль красная', 'Фасоль красная', 'Шпроты ж/б', 'Шпроты ст/б Экстра']

product_quantities = [93, 60, 75, 65, 90, 105, 57, 69, 69, 69, 59, 93, 95, 96, 69, 250, 105, 69, 69, 108, 59, 55, 57, 49, 105, 64, 139, 65, 149, 137, 69, 49, 49, 49, 49, 89, 117]

products = []

for i in range(len(product_names)):
    product = {'name': product_names[i], 'price': product_quantities[i]}
    products.append(product)



def add_products_to_db(products):
    if not Product.query.filter_by(initialized=True).first():
        for p in products:
            product = Product(name=p['name'], price=p['price'])
            db.session.add(product)
        Product.query.update({Product.initialized: True})
        db.session.commit()




from market.routes import index
if __name__ == '__main__':
    with app_ctx.app_context():
        db.create_all()
        add_products_to_db(products)
    app_ctx.run(debug=True)

