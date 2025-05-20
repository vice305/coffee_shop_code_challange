from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")


latte = Coffee("Latte")
espresso = Coffee("Espresso")


order1 = Order(alice, latte, 5.0)
order2 = Order(alice, espresso, 3.0)
order3 = Order(bob, latte, 6.0)


print(f"Alice's orders: {len(alice.orders())}") 
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")  
print(f"Bob's orders: {len(bob.orders())}") 

print(f"Latte orders: {latte.num_orders()}") 
print(f"Latte customers: {[customer.name for customer in latte.customers()]}")  
print(f"Latte average price: {latte.average_price()}")  

new_order = alice.create_order(espresso, 4.0)
print(f"New order price: {new_order.price}")  # Should print 4.0

top_customer = Customer.most_aficionado(latte)
print(f"Most aficionado for Latte: {top_customer.name if top_customer else None}")  # Should print Bob