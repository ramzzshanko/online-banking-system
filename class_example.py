class Constants:
    PI = 3.14159
    EULER = 2.71828
    GOLDEN_RATIO = 1.61803
    __ERROR_RATE = 10

    


print(Constants.PI)

print(Constants.__ERROR_RATE)

print(PI)


# Syntax of a class is simple
# class ClassName:
#   pass


class Refrigerator:

    def __init__(self, type, manufacturer):
        self.type = type
        self.manufacturer = manufacturer
        self.contents = []

    def add_contents(self, contents):
        self.contents.extend(contents)


_1000age = 1000
a100age = 100
__10age = 10

ref = Refrigerator("Upright", "Defy")

ref.__init__()


# camel casing e.g AnimalFood
# animal_food
# 

# pass = True