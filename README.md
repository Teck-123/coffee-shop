# coffee-shop

This is a backend developing code challenge that is built by creating three classes which include:
   - customer.py
   - coffee.py
   - order.py

The three files have a relationship through the use of *import*

## Features

* Customer.py - has a name (1-15 characters) and can also create orders
* Coffee.py - has a name (minimum 3 characters)
* Order.py - it links a customer to a coffee with a price
Theres also a validation with proper 'ValueError' messages
Aggregate methods: 'num_orders()', 'average_price()'
Association method: 'customer.create_order()'
Class method: 'customer.most_aficionado(coffee)' which returns the customer who spent the most on a given coffee

## The relationships

When the order is created it adds itself to the 
  - customer's order list
  - coffee's order list

Author: 
   - Thecla Owano
   