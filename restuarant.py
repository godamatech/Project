class Restuarant:
    """A simple Restuarant Class """

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served=0

    def describe_restuarant(self):
            return f"Restuarant Name: {self.name} \nCuisine Type: {self.cuisine_type}."

    def open_restuarant(self):
            # is_open=True
            return "Restuarant is opened!"
    def set_number_served(self, num):
        self.number_served = num 
        return self.number_served

    def increment_number_served(self, num):
        self.number_served += num 
        return self.number_served

