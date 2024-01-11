class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applly_raise(self)
        self.pay = int(self.pay * 1.04)
    
emp_1 = Employee('Edemialem', 'Tamiru', 4000)
emp_2 = Employee('alemu', 'kebede', 5999)


print(emp_1.pay)
print(emp_2.fullname())