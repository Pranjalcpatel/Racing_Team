# Design a class hierarchy to model geometric shapes.

# Shape Class (Base Class):

# __init__(self, color): This initializes the shape with its color.
# get_area(self): This is an abstract method (implement pass for now) that calculates the area of the shape. It should be implemented in derived classes.
# Rectangle Class:

# Inherits from Shape.
# __init__(self, color, width, height): This extends the shape initialization with width and height attributes.
# get_area(self): Overrides the base class method and calculates the area of the rectangle (width * height).
# ColoredDrawable (Mixin Class - Optional):

# This class is a mixin meant for inheritance, not direct object creation.
# __init__(self, color): Initializes the color attribute (similar to Shape).
# draw(self): This method simulates drawing the shape and prints "Drawing a {color} shape".
# Square Class:

# Inherits from Rectangle and optionally ColoredDrawable. (Use multiple inheritance here)
# __init__(self, color, side_length): This simplifies initialization by taking only the color and side length (which defines both width and height).
# Test Cases:

# Create a Rectangle object:

# Create a Rectangle object with color as "red", width as 5, and height as 10.
# Call get_area and verify it returns 50.
# Create a Square object:

# Create a Square object with color as "blue" and side_length as 4. (Consider using or not using ColoredDrawable in inheritance)
# Call get_area and verify it returns 16.
# (Optional) If using ColoredDrawable, call draw and verify it prints "Drawing a blue shape".
# Concepts Covered:

# Constructors: We use special methods __init__ to define constructors for each class, initializing their specific attributes.
# Multiple Inheritance: The Square class inherits from both Rectangle (for area calculation) and optionally ColoredDrawable (for drawing functionality).
# Abstract Methods: The get_area method in the Shape class is declared as abstract (using pass) to enforce implementation in derived classes.
# Bonus:

# Modify the Shape class to include an abstract method get_perimeter() and implement it in derived classes.

class Shape:
    def __init__(self,color):
        self.color=color
    def get_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, color, width, height):
        self.width=width
        self.height=height
    def get_area(self):
        self.area=self.width*self.height
        return self.area
class ColouredDrawable:
    def __init__(self, color):
        self.color=color
    def draw(self): 
        print(f"Drawing a {self.color} shape")
class Square(Rectangle,ColouredDrawable):
    def __init__(self, color, side_length):
        self.color=color
        self.width=side_length
        self.height=side_length


rect=Rectangle("red",5,10)
print(rect.get_area())
square=Square("blue",16)
print(square.get_area())
square.draw()