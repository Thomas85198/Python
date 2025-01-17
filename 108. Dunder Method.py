class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # define private method __key()
    def __key(self):
        return (self.name, self.name, self.address)

    # implement __hash__() function
    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"{self.name} is now {self.age} years old, living in {self.address}"

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, address {self.address}"

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented


robot1 = Robot("Wilson", 25, "Taiwan")
robot2 = Robot("Grace", 26, "Hawaii")

print(len(robot1))  # 6
print(robot1)  # Wilson is now 25 years old, living in Taiwan
print(repr(robot1))  # name: Wilson, age: 25, address Taiwan
print(robot1 + robot2)  # 51
