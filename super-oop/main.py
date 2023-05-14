class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square:
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return 4 * self.length


"""
In this example you have 2 shapes that are related to each other.
The code however, doesn't reflect that relationship and thus has code 
that is essentially repeated

By using inheritance you can reduce the amount of code you write while 
simultaneously reflecting the real-world relationship between rectangles 
and the squares
"""


class Rectangle2:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# here we declare that he Square2 class inherits from the Rectangle class
class Square2(Rectangle2):
    def __init__(self, length: int) -> None:
        # super() call the init() from the superClass
        super().__init__(length, length)


"""
You used super() to call the __init__() of the Rectangle2 class.
Allowing you to use it in the Square class without repeating code.
The core functionality remains after making changes
"""
square2 = Square2(2)
print(f"Ini are square2: {square2.area()}")
print(f"\nIni perimeter square2: {square2.perimeter()}")


class Cube(Square2):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


"""
Note: super() alone wont make the method calls for you: you have to call 
call the method on the proxy object itself
"""

"""
Cube doesn't have an __init__() because Cube inherits from Square2.
__init__() doesn't really do anythong differently for Cube that it already
does for Square2, you can skip defining it, and the __init__() of the 
superclass (Square) will be called automatically
"""

cube = Cube(3)
print(f"\nini surfacea_area cube: {cube.surface_area()}")
print(f"\nIni volume cube: {cube.volume()}")
