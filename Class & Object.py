class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start_engine(self):
        print("Engine started!")

    def stop_engine(self):
        print("Engine stopped!")

car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

print(car1.color)  # Output: Red
print(car2.brand)  # Output: Honda

car1.start()  # Output: The car has started.
car2.accelerate()  # Output: The car is accelerating.
