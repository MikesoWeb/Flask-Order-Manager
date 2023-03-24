# Flask Order Manager

Flask Order Manager is a web application for managing orders of products. It is built with Flask and SQLAlchemy.

## Features

- User authentication and authorization
- CRUD operations for orders and products
- Order details with total price calculation

## Installation

1. Clone the repository: `git clone https://github.com/MikesoWeb/Flask-Order-Manager.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Set the `FLASK_APP` environment variable: `export FLASK_APP=app.py`
4. Initialize the database: `flask db init`
5. Create the database tables: `flask db migrate` and `flask db upgrade`
6. Run the application: `flask run`

## Usage

1. Register a new user or log in with an existing account
2. Create products in the Products section
3. Create new orders in the Orders section by selecting products and specifying the quantity
4. View the details of an order in the Orders section, including the total price

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
