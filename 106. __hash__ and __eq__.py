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


robot = Robot("Wilson", 25, "Taiwan")
robot1 = Robot("Wilson", 25, "Taiwan")
robot2 = Robot("Grace", 26, "Hawaii")
print(robot == robot2)  # False
print(robot == robot1)  # True
dictionary = {robot: "Wilson"}
print(dictionary[robot])
