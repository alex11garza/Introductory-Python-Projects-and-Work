#  File: Employee.py
#  Student Name: Alex Garza
#  Student UT EID: ang3489


class Employee:

    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        self._name = kwargs['name']
        self._id   = kwargs['id']
        try:
            self._salary = kwargs['salary']
        except:
            self._salary = kwargs['salary'] = 0
               
    @property
    def salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._salary

    @salary.setter
    def salary(self, salary):
        pass
        '''##### ADD CODE HERE #####'''
        self._salary = salary

    @property
    def name(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._name

    @property
    def id(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._id

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary: {self._salary}"


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        super().__init__(**kwargs)
        self._salary = kwargs['salary']
        self._benefits = kwargs['benefits'] or []

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        if self._benefits == ["health_insurance",'retirement'] or self._benefits == ["retirement","health_insurance"]:
            return self._salary * 0.70
        elif self._benefits == ["health_insurance"]:
            return self._salary * 0.90
        elif self._benefits == ["retirement"]:
            return self._salary * 0.80
        else:
            return self._salary
            
    @property
    def benefits(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        pass
        '''##### ADD CODE HERE #####'''
        self._benefits = benefits

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary: {self._salary}\nBenefits: {', '.join(self._benefits)}\n"


############################################################
############################################################
############################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        super().__init__(**kwargs)
        self._salary = kwargs['salary']
        self._bonus  = kwargs['bonus']

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._salary + self._bonus

    @property
    def bonus(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._bonus

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary: {self._salary}\nBonus: {self._bonus}\n"

############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        super().__init__(**kwargs)
        self._salary = kwargs['salary']
        self._hours = kwargs['hours']

        

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        return self._salary * self._hours

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary per Hour: {self._salary}\nHours Worked: {self._hours}\n"


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        super().__init__(**kwargs)
        self._travel = kwargs['travel']
        self._name = kwargs['name']

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        return (super().cal_salary() + (self._travel*1000))

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary per Hour: {self._salary}\nHours Worked: {self._hours}\nTravel Expenses: {self._travel}\n"



############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        pass
        '''##### ADD CODE HERE #####'''
        super().__init__(**kwargs)
        self._bonus = kwargs['bonus']
        

    def cal_salary(self):
        pass
        '''##### ADD CODE HERE #####'''
        return super(Consultant_Manager, self).cal_salary() + self._bonus


    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f"Name: {self._name}\nID: {self._id}\nSalary per Hour: {self._salary}\nHours Worked: {self._hours}\nTravel Expenses: {self._travel}\n"



''' ##### DRIVER CODE #####
    ##### Do not change. '''


def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary with health insurance is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary with health insurance and reirement is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary with no benefits is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()