class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print ("The car has started.")


# Creating an instance of the Car class
car1 = Car ("Red", "Toyota")

# Accessing the attributes of the car object
print (car1.color)  # Output: Red
print (car1.brand)  # Output: Toyota

# Calling the start() method of the car object
car1.start ()  # Output: The car has started.
