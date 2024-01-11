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


class Developer(Employee):
    raise_amt = 1.10
 
    def __init__(self, first, last, pay, prog):
        super().__init__(first, last, pay)
        self.prog = prog


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.num_employee = []
        else:
            self.num_employee = employee 
    def add_emp(self, emp):
        if emp not in self.num_employee:
            self.num_employee.append(emp)
    def remove_emp(self, emp):
        if emp in self.num_employee:
            self.num_employee.remove(emp)
    def print_emps(self):
        for emp in self.num_employee:
            print('--->', emp.fullname())

dev_1 = Developer('Edemialem', 'Tamiru', 4000, 'python')
dev_2 = Developer('alemu', 'kebede', 5999,'java' )


mgr_1 = Manager('age', 'tamiru', 68688, [dev_1])


# print(Employee.__dict__.applly_raise())
print(dev_1.email)
print(dev_2.email)
print(mgr_1.email)
mgr_1.print_emps()


# print(help(Developer))

