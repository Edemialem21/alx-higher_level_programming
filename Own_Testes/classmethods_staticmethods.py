class Employee:
    raise_amt = 1.04
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
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_srt_1.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Edemialem', 'Tamiru', 4000)
emp_2 = Employee('alemu', 'kebede', 5999)
emp_srt_1 = 'getachew-tamiru-60000'

Employee.set_raise_amt(1.05)

new_emp1 = Employee.from_string(emp_srt_1)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)



print(emp_1.fullname())
# print(Employee('Edemialem', 'Tamiru', 4000).email)
print(emp_1.email)
print(emp_1.pay)
print(emp_2.fullname())
print(Employee.num_employe)

import datetime
my_date = datetime.date(2024, 1, 15)
print(Employee.is_workday(my_date))