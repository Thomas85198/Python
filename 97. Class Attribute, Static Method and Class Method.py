
# class Robot:
#     ingredient = "metal"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def greet():
#         print("A robot says hi...")

#     # def walk(self):
#     #     print(f"{self.name} is walking")

#     # def greet(self):
#     #     print(f"Hi, My name is {self.name}, and I am made of {
#     #           self.__class__.ingredient}")


# my_robot_1 = Robot("Wilson", 25)
# # print(my_robot_1.ingredient)  # Output: metal
# # my_robot_1.greet()  # Output: Hi, My name is Wilson, and I am made of metal

# Robot.greet()  # Output: A robot says hi...
# my_robot_1.greet()  # Output: A robot says hi...

class Circle:
    """This class creates circle"""
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total

    @classmethod
    def total_area_2(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


c1 = Circle(10)
c2 = Circle(15)

print(c1.area())  # 輸出單個圓的面積
print(c1.__class__.total_area())  # 所有圓的總面積（靜態方法）
print(c1.__class__.total_area_2())  # 所有圓的總面積（類別方法）
print(c1.total_area())  # 所有圓的總面積（靜態方法）
print(c1.total_area_2())  # 所有圓的總面積（類別方法）
