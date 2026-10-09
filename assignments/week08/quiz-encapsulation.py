"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def get_area(self):
    return f"area : width {self.width} and length {self.length} = {self.width * self.length}"

  def get_perimeter(self):
    return f"Perimeter : width {self.width} and length {self.length} = {2 * (self.width + self.length)}"

  def isSquare(self):
    return self.width == self.length


myrectangle = Rectangle(5, 10)
print(myrectangle.get_area())