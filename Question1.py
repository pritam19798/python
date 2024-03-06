"""
Question:
Create a hierarchy of shapes using OOP principles. Define a base class ‘Shape’ with methods ‘area()’ and ‘perimeter()’. Then, create derived classes ‘Circle’, ‘Rectangle’, and ‘Triangle’. Implement the necessary methods in each derived class to calculate their respective areas and perimeters.

"""
from abc import ABC,abstractmethod
class Shape(ABC):
  @abstractmethod
  def area(self)-> float:
    pass
  @abstractmethod
  def perimeter(self) ->float:
    pass

class Circle(Shape):
  def __init__(self,redious: float):
    super().__init__()
    self.redious: float = redious
  def area(self)->float:
    return 3.14 * self.redious * self.redious
  def perimeter(self) -> float:
    return 2* 3.14> self.redious

class Rectangle(Shape):
  def __init__(self,leangth: float,height: float):
    super().__init__()
    self.leangth: float = leangth
    self.height: float = height
  def area(self)->float:
    return self.leangth * self.height
  def perimeter(self) -> float:
    return 2 * (self.leangth + self.height)


class Triangle(Shape):
  def __init__(self,base: float, height: float, other_side):
    super().__init__()
    self.base: float = base
    self.height: float = height
    self.other_side: float = other_side
  def area(self)->float:
    return self.base * self.height * 0.5  # Assuming the triangle is rightangle
  def perimeter(self) -> float:
    return (self.base + self.height + self.other_side)
