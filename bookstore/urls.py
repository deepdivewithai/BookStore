from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('books/', views.BooksListView.as_view()),
    path('customers/', views.CustomerListView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('order_details/', views.OrderDetailListView.as_view())
]
