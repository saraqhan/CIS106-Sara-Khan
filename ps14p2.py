class Student:
  def __init__(self, first, last, dist, encrd):
    self.first = first
    self.last = last
    self.dist = dist
    self.encrd = encrd

  def tuitionowed(self):
    indistrate = 250.00
    outdistrate = 500.00

    if self.dist == "I":
      tutionrate = indistrate
    else:
      tutionrate = outdistrate

    tuitionowed = self.encrd * tutionrate
    return tuitionowed

student1 = Student('Sam', 'Smith', 'I', 12)
student2 = Student('Michael', 'Read', 'O', 15)

def info(student):
  print(student.first, ' ', student.last + ':')
  print('District Code:', student.dist)
  print('Enrollment Credits:', student.encrd)
  print('Tuition Owed: $', format(student.tuitionowed(), ',.2f') + '\n')

info(student1)
info(student2)