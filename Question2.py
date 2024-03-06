"""
Question:
Implement a simple student and course management system using OOP. Create classes ‘Student’ and ‘Course’. The ‘Student’ class should have attributes for student details (name, ID, etc.) and a method to calculate the GPA. The ‘Course’ class should have a list of enrolled students and methods to add a student, remove a student, and calculate the average GPA of all students in the course
"""

from typing import List
from abc import ABC,abstractmethod
class BaseStudent(ABC):
  def __init__(self,name: str, id: str):
    self.name:str = name
    self.id: str = id
  @abstractmethod
  def calculate_gpa() -> int:
    pass 
class BaseCourse(ABC):
  def __init__(self,students: List[BaseStudent]):
    self.students:List[BaseStudent] = students

  @abstractmethod
  def add_students(self,student:BaseStudent):
    pass

  @abstractmethod
  def remove_students(self):
    pass

  @abstractmethod
  def average_gpa(self) ->float:
    pass

class Student(BaseStudent):
  def __init__(self,name: str, id: str,gpa1:int, gpa2: int):
    super().__init__(name,id)
    self.subject1_gpa: int = gpa1
    self.subject12_gpa: int = gpa2

  def calculate_gpa(self) -> int:
    return (self.subject1_gpa + self.subject12_gpa) //2

class Course(BaseCourse):
  def __init__(self,students: List[BaseStudent], name: str):
    super().__init__()
    self.name: str = str


  def add_students(self,student:BaseStudent):
    self.students.append(student)

  def remove_students(self, student: BaseStudent):
    self.students.remove(student)


  def average_gpa(self) ->float:
    total: int = 0
    for student in self.students:
      total = total +student.calculate_gpa()
    return total / len(self.students)
