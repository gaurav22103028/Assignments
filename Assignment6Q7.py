class Student:
  pass

class Marks:
  pass

student1 = Student()
marks1 = Marks()

print("Student 1 is instance of Student class :", isinstance(student1, Student))
print("Marks 1 is instance of Marks class :", isinstance(marks1, Marks))

print("Student is subclass of class object :", issubclass(Student, object))
print("Marks is subclass of class object :", issubclass(Marks, object))