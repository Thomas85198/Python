# class Robot:
#     pass


# my_robot = Robot()
# print(type(my_robot))  # Output: <class '__main__.Robot'>

class Robot:
    # in classes, we can also define doctring
    """Robot class is for creation robots"""
    # Constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")


my_robot_1 = Robot("Wilson", 25)

print(my_robot_1.__doc__)  # Output: Robot class is for creation robots
my_robot_1.walk()  # Output: Wilson is walking
