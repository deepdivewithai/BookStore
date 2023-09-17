from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    publication_year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    @classmethod
    def books_published_in_year(cls, year):
        return cls.objects.filter(publication_year=year).values('title', 'author')
    
    @classmethod
    def average_price_before(cls,year):
        from django.db.models import Avg
        return cls.objects.filter(publication_year__lt=year).aggregate(average_price=Avg('price'))['average_price']
    
    @classmethod
    def books_with_lowest_stock(cls):
        from django.db.models import Min, F
        return cls.objects.annotate(min_stock=Min('available_quantity')).filter(available_quantity=F('min_stock')).order_by('min_stock')[:20]



class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    registration_date = models.DateField()

    @classmethod
    def customer_with_highest_purchase(cls):
        from django.db.models import Sum
        return cls.objects.annotate(total_spent=Sum('order__total_amount')).order_by('-total_spent').first()
    
    @classmethod
    def customer_registered_in_year(cls, year):
        return cls.objects.filter(registration_date__year=year)
    
    @classmethod
    def customers_with_most_orders(cls):
        from django.db.models import Count
        return cls.objects.annotate(total_orders=Count('order')).order_by('-total_orders')[:5]



class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    @classmethod
    def revenue_by_year(cls, year1, year2):
        from django.db.models.functions import ExtractYear
        from django.db.models import Sum
        return cls.objects.annotate(order_year=ExtractYear('order_date'))  \
            .filter(order_year__range=(year1, year2)).values('order_year').annotate(total_revenue=Sum('total_amount'))



class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    @classmethod
    def top_bestsellers(cls):
        from django.db.models import Sum
        return cls.objects.values('book_id__title', 'book_id__author').annotate(total_sold=Sum('quantity')).order_by('-total_sold')[:5]
    
    
    @classmethod
    def total_revenue_for_year(cls, year):
        from django.db.models import Sum
        return cls.objects.filter(order_id__order_date__year=year).aggregate(total_revenue=Sum('subtotal'))['total_revenue']


        

