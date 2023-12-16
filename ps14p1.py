
class Employee:
  def __init__(self, first, last, pay, salary):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
    self.salary = salary



  def bonus(self,rate):
    b = float(rate) * float(self.pay)
    return b



empl1 = Employee('Sara', 'Khan',60000.00,75000.00)

print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.salary)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))
