class Dog:
    # Constructor - initializes the dog's name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says: Woof!")

# Create an instance of the Dog class
dog1 = Dog("Buddy", 2)

# Access attributes and call methods of the dog object
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()









# explaining init method
class MyClass:
    def __init__(self, arg1, arg2, ...):
        # Initialization code here
        self.attribute1 = arg1
        self.attribute2 = arg2
        # ...









# init example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30







# pizza maker class 
class PizzaMaker:
    def __init__(self):
        self.pizza = []

    def add_base(self, base):
        self.pizza.append(f"Base: {base}")

    def add_sauce(self, sauce):
        self.pizza.append(f"Sauce: {sauce}")

    def add_cheese(self, cheese):
        self.pizza.append(f"Cheese: {cheese}")

    def add_topping(self, topping):
        self.pizza.append(f"Topping: {topping}")

    def bake(self):
        print("Baking the pizza...")

    def display_pizza(self):
        print("Pizza ingredients:")
        for ingredient in self.pizza:
            print(ingredient)


# Create an instance of the PizzaMaker class
pizza_maker = PizzaMaker()

# Adding ingredients to the pizza
pizza_maker.add_base("Thin crust")
pizza_maker.add_sauce("Tomato sauce")
pizza_maker.add_cheese("Mozzarella")
pizza_maker.add_topping("Mushrooms")
pizza_maker.add_topping("Pepperoni")

# Display the pizza ingredients
pizza_maker.display_pizza()

# Bake the pizza
pizza_maker.bake()






# method using other methods
class PizzaMaker:
    def __init__(self):
        self.pizza = []

    def add_base(self, base):
        self.pizza.append(f"Base: {base}")

    def add_sauce(self, sauce):
        self.pizza.append(f"Sauce: {sauce}")

    def add_cheese(self, cheese):
        self.pizza.append(f"Cheese: {cheese}")

    def add_topping(self, topping):
        self.pizza.append(f"Topping: {topping}")

    def bake(self):
        print("Baking the pizza...")

    def display_pizza(self):
        print("Pizza ingredients:")
        for ingredient in self.pizza:
            print(ingredient)

    def prepare_pizza(self):
        self.add_base("Thin crust")
        self.add_sauce("Tomato sauce")
        self.add_cheese("Mozzarella")
        self.add_topping("Mushrooms")
        self.add_topping("Pepperoni")
        print("Pizza is ready to be baked!")

# Create an instance of the PizzaMaker class
pizza_maker = PizzaMaker()

# Prepare the pizza using the prepare_pizza method
pizza_maker.prepare_pizza()

# Display the pizza ingredients
pizza_maker.display_pizza()

# Bake the pizza
pizza_maker.bake()





#inheritance and extending attributes
# Base class (superclass) - Animal
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

    def show_species(self):
        print(f"I am a {self.species}")


# Subclass - Dog, inheriting from Animal
class Dog(Animal):
    def __init__(self, breed, name):
        # Call the constructor of the superclass
        super().__init__("Dog")
        self.breed = breed
        self.name = name

    # Overriding the make_sound method
    def make_sound(self):
        print("Woof!")

    def show_info(self):
        print(f"I am a {self.breed} named {self.name}")


# Create an instance of the Dog class
dog1 = Dog("Labrador", "Buddy")

# Access attributes and call methods from both classes
dog1.show_species()  # Output: I am a Dog
dog1.show_info()     # Output: I am a Labrador named Buddy
dog1.make_sound()    # Output: Woof!
