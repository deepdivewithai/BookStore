from django.contrib import admin
from .models import Customer, Book, OrderDetail, Order

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(OrderDetail)
admin.site.register(Order)