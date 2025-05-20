from customer import Customer
from coffee import Coffee
from order import Order

def test_customer():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    try:
        customer.name = "A" * 16  
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("Customer tests passed!")

test_customer()