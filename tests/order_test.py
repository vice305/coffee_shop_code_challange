from order import Order
from customer import Customer
from coffee import Coffee

def test_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.price == 5.0
    assert order.customer == customer
    assert order.coffee == coffee
    try:
        order.price = 11.0  
        assert False, "Price should be immutable"
    except AttributeError:
        pass
    print("Order tests passed!")

test_order()