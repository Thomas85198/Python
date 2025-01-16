class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25

    def greet(self):
        print(f"Hi, I am {self.__age} years old.")
        self.__this_is_private()

    # private method
    def __this_is_private(self):
        print("Hello from private method.")


my_robot = Robot("Wilson")
# print(my_robot.__age)  # AttributeError: 'Robot' object has no attribute '__age'
my_robot.greet()  # Hi, I am 25 years old. Hello from private method.

