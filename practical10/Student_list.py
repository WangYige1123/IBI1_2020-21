class Student:
  def __init__(self,first_name,last_name,programme):
    self.first_name = first_name
    self.last_name = last_name
    self.programme = programme
  def f(self):
    print(self.first_name + self.last_name + '\n' + self.programme)
c = Student('Wang','Yige','BMI')
c.f()
