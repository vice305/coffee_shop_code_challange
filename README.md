#Coffee Shop Code Challenge

This project implements a Coffee Shop domain model in Python, featuring Customer, Coffee, and Order classes with object relationships and aggregate methods as part of a Moringa School assignment. It demonstrates a many-to-many relationship between Customer and Coffee through Order, with validations and a bonus method.

File Structure

customer.py: Defines the Customer class with name validation, order/coffee relationships, and most_aficionado() method.

coffee.py: Defines the Coffee class with name validation, order/customer relationships, and aggregate methods.

order.py: Defines the Order class with customer, coffee, and price validation, storing all orders.

debug.py: Test script to verify functionality with sample data.

tests/customer_test.py: Tests for Customer class.

tests/coffee_test.py: Tests for Coffee class.

tests/order_test.py: Tests for Order class.

NOTES

This project fulfills the requirements of the Coffee Shop Code Challenge, including model initializers, properties, relationships, aggregates, and the bonus method.

Lazy imports are used in customer.py and coffee.py to avoid circular imports.



