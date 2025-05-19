class Order:
    def __init__(self , customer, coffees):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffees, list):
            raise TypeError("coffees must be a list")
        if not all(isinstance(coffee, Coffee) for coffee in coffees):
            raise TypeError("all items in coffees must be Coffee instances")
        self.customer = customer
        self.coffees = coffees
        