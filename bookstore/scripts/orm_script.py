from bookstore.models import Book, Customer, Order, OrderDetail
from datetime import date
from faker import Faker
import random

fake = Faker()

def run():
    print('Hello from scripts!!')

    books_to_insert = [
    Book(title='Book 1', author='Author A', publication_year=2022, price=19.99, available_quantity=50),
    Book(title='Book 2', author='Author B', publication_year=2022, price=15.99, available_quantity=30),
    Book(title='Book 3', author='Author C', publication_year=2020, price=24.99, available_quantity=20),
    Book(title='Book 4', author='Author D', publication_year=2019, price=12.99, available_quantity=10),
    Book(title='Book 5', author='Author E', publication_year=2021, price=29.99, available_quantity=5),
    Book(title='Book 6', author='Author F', publication_year=2018, price=14.99, available_quantity=15),
    Book(title='Book 7', author='Author G', publication_year=2000, price=18.99, available_quantity=25),
]

    Book.objects.bulk_create(books_to_insert)

    customers_to_insert = [
    Customer(first_name='Miles', last_name='Shane', email='miles.shane@gmail.com', registration_date='2022-01-15'),
    Customer(first_name='Alice', last_name='Smith', email='alice.smith@example.com', registration_date='2021-03-10'),
    Customer(first_name='Bob', last_name='Johnson', email='bob.johnson@example.com', registration_date='2022-05-20'),
    Customer(first_name='Eva', last_name='Clark', email='eva.clark@example.com', registration_date='2023-02-28'),
]

    Customer.objects.bulk_create(customers_to_insert)

    orders_to_insert = [
    Order(customer_id=Customer.objects.get(id=1), order_date='2022-12-10', total_amount=39.98),
    Order(customer_id=Customer.objects.get(id=2), order_date='2022-11-05', total_amount=35.97),
    Order(customer_id=Customer.objects.get(id=3), order_date='2022-10-20', total_amount=74.97),
    Order(customer_id=Customer.objects.get(id=4), order_date='2023-01-05', total_amount=99.99),
    Order(customer_id=Customer.objects.get(id=1), order_date='2021-12-01', total_amount=15.99),
]

    Order.objects.bulk_create(orders_to_insert)

    order_details_to_insert = [
    OrderDetail(order_id=Order.objects.get(id=1), book_id=Book.objects.get(id=1), quantity=2, subtotal=39.98),
    OrderDetail(order_id=Order.objects.get(id=2), book_id=Book.objects.get(id=2), quantity=1, subtotal=15.99),
    OrderDetail(order_id=Order.objects.get(id=3), book_id=Book.objects.get(id=3), quantity=3, subtotal=74.97),
    OrderDetail(order_id=Order.objects.get(id=4), book_id=Book.objects.get(id=4), quantity=1, subtotal=12.99),
    OrderDetail(order_id=Order.objects.get(id=5), book_id=Book.objects.get(id=5), quantity=2, subtotal=59.98),
    OrderDetail(order_id=Order.objects.get(id=1), book_id=Book.objects.get(id=3), quantity=1, subtotal=12.99),
    OrderDetail(order_id=Order.objects.get(id=2), book_id=Book.objects.get(id=1), quantity=2, subtotal=39.98),
    OrderDetail(order_id=Order.objects.get(id=3), book_id=Book.objects.get(id=2), quantity=1, subtotal=15.99),
    OrderDetail(order_id=Order.objects.get(id=4), book_id=Book.objects.get(id=5), quantity=3, subtotal=89.97),
    OrderDetail(order_id=Order.objects.get(id=5), book_id=Book.objects.get(id=4), quantity=1, subtotal=29.99),
]

    OrderDetail.objects.bulk_create(order_details_to_insert)
    print('Script completed!')