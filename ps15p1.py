class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b

class Manager(Employee):
  def ltbonus(self):
    return 0.4 * float(self.pay)

manager1 = Manager('Vanessa', 'Jane', 80000.00)

print("Manager Information:")
print("Email:", manager1.email)
print("First Name:", manager1.first)
print("Last Name:", manager1.last)
print("Salary:", manager1.pay)
print("Bonus 10%:", manager1.bonus(0.10))
print("Long term bonus:", manager1.ltbonus())