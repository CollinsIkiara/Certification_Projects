# Polygon Area Calculator

# This program defines two classes, Rectangle and Square, to calculate the area, perimeter, diagonal, and other properties of these shapes. The classes also include methods to set dimensions and generate a visual representation of the shapes using asterisks. Additionally, the program includes test cases to demonstrate the functionality of the classes.

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self.width = length
        self.height = length

    def __repr__(self):
        return f"Square(side={self.width})"


# --- Example Usage ---
rect = Rectangle(10, 5)
print(rect.get_area())        # 50
rect.set_height(3)
print(rect.get_perimeter())   # 26
print(rect)                   # Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********

sq = Square(9)
print(sq.get_area())          # 81
sq.set_side(4)
print(sq.get_diagonal())      # 5.656854249492381
print(sq)                     # Square(side=4)
print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8

print("--- Test Cases ---")
print(Rectangle(3, 6))                          # Rectangle(width=3, height=6)
print(Square(5))                                # Square(side=5)
print(Rectangle(3, 6).get_area())              # 18
print(Square(5).get_area())                    # 25
print(Rectangle(3, 6).get_perimeter())         # 18
print(Square(5).get_perimeter())               # 20
print(Rectangle(3, 6).get_diagonal())          # 6.708203932499369
print(Square(5).get_diagonal())                # 7.0710678118654755
print(Rectangle(15, 10).get_amount_inside(Square(5)))       # 6
print(Rectangle(4, 8).get_amount_inside(Rectangle(3, 6)))   # 1
print(Rectangle(2, 3).get_amount_inside(Rectangle(3, 6)))   # 0

big_rect = Rectangle(51, 10)
print(big_rect.get_picture())   # Too big for picture.

r = Rectangle(3, 6)
r.set_width(10)
r.set_height(20)
print(r)                        # Rectangle(width=10, height=20)

s = Square(5)
s.set_side(9)
print(s)                        # Square(side=9)

s2 = Square(5)
s2.set_width(3)
print(s2)                       # Square(side=3)