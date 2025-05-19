class Cutomer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name cannot be empty")
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value:
            raise ValueError("name cannot be empty")
        self.__name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]
        
        