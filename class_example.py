class Constants:
    PI = 3.14159
    EULER = 2.71828
    GOLDEN_RATIO = 1.61803


print(Constants.PI)


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

    