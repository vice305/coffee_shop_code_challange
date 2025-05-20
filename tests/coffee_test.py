from coffee import Coffee

def test_coffee():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    try:
        coffee.name = "Espresso" 
        assert False, "Name should be immutable"
    except AttributeError:
        pass
    print("Coffee tests passed!")

test_coffee()