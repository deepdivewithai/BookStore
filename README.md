# Online Bookstore Database Case Study

In this case study, we will analyze an online bookstore's database with several tables: Books, Customers, Orders, and Order_Details. We will perform various SQL queries to extract valuable information from the database.

## Database Tables

1. **Books**: Contains information about books.
   - `book_id` (Primary Key)
   - `title`
   - `author`
   - `publication_year`
   - `price`
   - `available_quantity`

2. **Customers**: Contains customer information.
   - `customer_id` (Primary Key)
   - `first_name`
   - `last_name`
   - `email`
   - `registration_date`

3. **Orders**: Contains order details.
   - `order_id` (Primary Key)
   - `customer_id` (Foreign Key)
   - `order_date`
   - `total_amount`

4. **Order_Details**: Contains information about individual book items within each order.
   - `order_id` (Foreign Key)
   - `book_id` (Foreign Key)
   - `quantity`
   - `subtotal`

## Tasks and SQL Queries

1. Retrieve a list of books (book title and author) published in the year 2022.
   ```sql
   SELECT title, author
   FROM Books
   WHERE publication_year = 2022;
   ```

2. Calculate the total revenue generated by the bookstore in the year 2022.
   ```sql
   SELECT SUM(total_amount) AS total_revenue
   FROM Orders
   WHERE YEAR(order_date) = 2022;
   ```

3. Find the top 5 bestselling books (based on the total quantity sold) in descending order.
   ```sql
   SELECT b.title, b.author, SUM(od.quantity) AS total_quantity_sold
   FROM Books b
   JOIN Order_Details od ON b.book_id = od.book_id
   GROUP BY b.title, b.author
   ORDER BY total_quantity_sold DESC
   LIMIT 5;
   ```

4. Determine the customer who made the highest total purchase amount and the total amount they spent.
   ```sql
   SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_purchase_amount
   FROM Customers c
   JOIN Orders o ON c.customer_id = o.customer_id
   GROUP BY c.first_name, c.last_name
   ORDER BY total_purchase_amount DESC
   LIMIT 1;
   ```

5. Calculate the average price of books published before the year 2010.
   ```sql
   SELECT AVG(price) AS average_price
   FROM Books
   WHERE publication_year < 2010;
   ```

6. Identify the customer(s) who registered in 2023.
   ```sql
   SELECT first_name, last_name
   FROM Customers
   WHERE YEAR(registration_date) = 2023;
   ```

7. Calculate the total number of orders placed in the database.
   ```sql
   SELECT COUNT(*) AS total_orders
   FROM Orders;
   ```

8. Find the book(s) with the lowest available quantity in stock.
   ```sql
   SELECT title, author, MIN(available_quantity) AS lowest_quantity
   FROM Books;
   ```

9. Calculate the total revenue for each year from 2020 to 2022.
   ```sql
   SELECT YEAR(order_date) AS year, SUM(total_amount) AS total_revenue
   FROM Orders
   WHERE YEAR(order_date) BETWEEN 2020 AND 2022
   GROUP BY YEAR(order_date);
   ```

10. Determine the customer(s) with the most orders placed.
    ```sql
    SELECT c.first_name, c.last_name, COUNT(o.order_id) AS total_orders_placed
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    GROUP BY c.first_name, c.last_name
    ORDER BY total_orders_placed DESC;
    ```

# Switching to Django ORM
Now, let's switch to using Django ORM (Object-Relational Mapping) for the same tasks. Below, I'll present the equivalent Django ORM code for these tasks.

1. **Books**: Contains information about books.
![Bookstore](https://github.com/deepdivewithai/BookStore/raw/main/Django%20Bookstore%20Images/Book.png)

2. **Customers**: Contains customer information.
![Bookstore](https://github.com/deepdivewithai/BookStore/raw/main/Django%20Bookstore%20Images/Customer.png)
