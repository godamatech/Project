class Restuarant:
    """A simple Restuarant Class """

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
            return f"Restuarant Name: {self.name} \nCuisine Type: {self.cuisine_type}."

    def open_restuarant(self):
            # is_open=True
            return "Restuarant is opened!"
    
print("======   Restuarant   ======")
restuarant=Restuarant("Mr. Biggs", "Cuisine type A")
print(restuarant.name)
print(restuarant.cuisine_type)
print()
print(restuarant.describe_restuarant())
print()
print(restuarant.open_restuarant())

print("======   Three Restuarants   ======")
restuarant1=Restuarant("Mr. Biggs", "Cuisine type-A")
restuarant2=Restuarant("Chiken Republic", "Cuisine type-B")
restuarant3=Restuarant("Tasty Restuarants", "Cuisine type-C")
print(restuarant1.describe_restuarant())
print()
print(restuarant2.describe_restuarant())
print()
print(restuarant3.describe_restuarant())
print()


print("======   User Class   ======")
class User:
    """simple User class"""
    
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile=user_profile

    def describe_user(self):
        return f"My name is {self.first_name} {self.last_name}\nOther characters:{[i for i in self.user_profile]} ."
    
    def greet_user(self):
        return f"Hi {self.last_name.upper()}!"


user1=User("Abdullahi","Bello","kano","Hausa")
print(user1.describe_user())
print()
print(user1.greet_user())

print()
user2=User("Tijjani","Muhammad","kaduna","Ibira")
print(user2.describe_user())
print()
print(user2.greet_user())

print()
user3=User("Hassan","Muhammad","kano","Hausa")
print(user3.describe_user())
print()
print(user3.greet_user())

print()
print("======  Modifying Restuarant class ======")
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

r=Restuarant("Pluto's Restuarant", "Cuisine Type-A")
print(f"Initial Number of customers served: {r.number_served}")

r.number_served = 23
print(f"Changed Number of customers served : {r.number_served}")
print(f"Changed Number of customers served through method: {r.set_number_served(23_000)}")
print(f"Incremented Number of customers served through method: {r.increment_number_served(2_000)}")

print()
print("======  Modifying User Class   ======")
class User:
    """simple User class"""
    
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile=user_profile
        self.login_attempts=0

    def describe_user(self):
        return f"My name is {self.first_name} {self.last_name}\nOther informations:{[i for i in self.user_profile]} ."
    
    def greet_user(self):
        return f"Hi {self.last_name.upper()}!"

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


u = User("Hassan","Muhammad","kano","Hausa")
print(f"Initial Number of login attempts: {u.login_attempts}")
print(f"Incremented Number of login attempts: {u.increment_login_attempts()}")
print(f"Another Incremented Number of login attempts: {u.increment_login_attempts()}")
print(f"Reset Number of login attempts: {u.reset_login_attempts()}")

print()
print("======  Ice Cream Stand Class   ======")
class IceCreamStand(Restuarant):
    """This an ice cream class that inherit from the restuarant class"""

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Butter Pecan']

    def display_flavors(self):
        print("List of Flavors are:")
        for flavor in self.flavors:
            print(f" - {flavor}")
        return ""


ice = IceCreamStand("Ice-Cream Palace", "Traditional Chinese Food")
print(ice.display_flavors())


print()
print("======  Privileges Class   ======")
class Privilege:
    """This class models privilages of an admin"""

    def __init__(self, privilages=['can add post', 'can delete post', 'can ban user', 
            'Create User', 'Update User', 'Display User\'s information ', 'Delete User', ]
            ):
        self.privilages = privilages

    def show_privileges(self):
        print("List of Admin Privileges are:")
        for privilege in self.privilages:
            print(f" - {privilege}")
        return ""


print()
print("======  Admin Class   ======")
class Admin(User):
    """This an Admin model that inherit from the User class""" 

    def __init__(self, first_name, last_name, *user_profile):
        super().__init__(first_name, last_name, *user_profile)
        self.privileges = Privilege()

    
admin = Admin("Abdullahi","Bello","kano","Hausa")
admin.privileges.show_privileges()
print()


print()
print("======  Car Class   ======")
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


print()
print("======  Battery Class   ======")
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return f"This car has a {self.battery_size}-kWh battery."

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range=0
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        return f"This car can go about {range} miles on a full charge."

    def upgrade_battery(self):
        self.battery_size = 100
        return self.battery_size



# 
print()
print("======  Electric Car Class   ======")
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, battery_size=75):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.battery = Battery()

        def describe_battery(self):
            """Print a statement describing the battery size."""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def fill_gas_tank(self):
            """Electric cars don't have gas tanks."""
            print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

    
# Battery Upgrade
print()
print("======  Battery Upgrade    ======")
my_tesla = ElectricCar('Toyota', 'Accord', 2021)
print(my_tesla.battery.get_range())
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())
print()

