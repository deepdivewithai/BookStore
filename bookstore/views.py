from django.shortcuts import render
from .models import Book, OrderDetail, Customer
from rest_framework.generics import ListCreateAPIView
from .serializers import *

class BooksListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

class CustomerListView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailListView(ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailsSerializer


def all_tasks_view(request):

    books_in_2022 = Book.books_published_in_year(2022)

    average_price_before_2010 = Book.average_price_before(2010)

    books_with_lowest_stock = Book.books_with_lowest_stock()

    customer_highest_purchase = Customer.customer_with_highest_purchase()

    customers_registered_in_2023 = Customer.customer_registered_in_year(2023)

    total_orders = Order.objects.count()

    revenue_in_2022 = OrderDetail.total_revenue_for_year(2022)

    top_bestsellers = OrderDetail.top_bestsellers()

    revenue_2020_to_2022 = Order.revenue_by_year(2020, 2022)

    customers_with_most_orders = Customer.customers_with_most_orders()

    context = {
        'books_in_2022': books_in_2022,
        'average_price_before_2010': average_price_before_2010,
        'books_with_lowest_stock': books_with_lowest_stock,
        'customer_highest_purchase': customer_highest_purchase,
        'customers_registered_in_2023': customers_registered_in_2023,
        'total_orders': total_orders,
        'revenue_in_2022': revenue_in_2022,
        'top_bestsellers': top_bestsellers,
        'revenue_2020_to_2022': revenue_2020_to_2022,
        'customers_with_most_orders': customers_with_most_orders,
    }

    return render(request, 'tasks.html', context)


