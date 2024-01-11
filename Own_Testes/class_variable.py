class Employee:
    raise_amount = 1.04
    num_employe = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employe += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applly_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee('Edemialem', 'Tamiru', 4000)
emp_2 = Employee('alemu', 'kebede', 5999)

print(emp_1.fullname())
# print(Employee('Edemialem', 'Tamiru', 4000).email)
print(emp_1.email)
print(emp_1.pay)
print(emp_2.fullname())
print(Employee.num_employe)