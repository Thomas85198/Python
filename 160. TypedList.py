class TypedList:
    def __init__(self, example_element, initial_list):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)
        self.element = initial_list[:]  # Copy the list by value

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError(
                "Attempted to add an element of incorrect type to a typed list.")

    def __setitem__(self, i, element):
        self.__check(element)
        self.element[i] = element

    def __getitem__(self, i):
        return self.element[i]

    def __str__(self):
        return str(self.element)


x = TypedList(1, [1, 2, 3, 4, 5])
print(x)
