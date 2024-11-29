#Jordan Faulkner 
# 6-4-2024
#Short projecting displaying knowledge of Encapsulation, Inheritance, and Polymorphism using Object Oriented Programming in Python. 
#Creating an Employee class using OOP in Python 
class Employee():
    MINIMUM_SALARY = 30000 #Class Variable 
    CURRENT_YEAR = 2024 #Class variable 
    def __init__(self,salary=0,name='',emp_code = '',position = '',birth_year = 0): #Class Constructor 
        self.name = name 
        self.emp_code = emp_code
        self.position = ''
        self.birth_year = birth_year
        if salary<=self.MINIMUM_SALARY: #Using the class variable in a method 
            self.salary = salary 
        else:
            self.salary = 0
            print("Invalid Salary Entry!")
    def __str__(self): #__str__ method for object string representation to the end user 
      emp_str = f"""Employee name: {self.name}
                Employee salary: {self.salary}"""
      return emp_str
    def set_salary(self,new_salary):
        self.salary = new_salary
    def give_raise(self,amount):
        self.salary+=amount 
        print(f'Congratulations! You have recieved a raise of ${amount}.00!')
    def set_empcode(self,code):
        self.emp_code = str(code)
        print(f'Your employee code number has been set to: {code}.')
    def set_position(self,role):
        self.position = str(role)
        print(f"The employee {self.name} has the current role of {role}.")
    @classmethod #initializing a class method using cls instead of self. cls is short for class 
    def emp_age(cls,name,birth_year):
        age = Employee.CURRENT_YEAR - birth_year
        print(f"The Employee is, or is almost: {age} years old.")
        return cls(age)
class Manager(Employee): #First instance of inheritance. Manager is the child class, Employee is the parent class 
    def __init__(self,name = '',position='',salary=0):
        Employee.__init__(self,salary=0,name='',emp_code = '',position = '',birth_year = 0) #must call the parent instructor in the child class constructor
        self.name = name
        self.position = position 
        self.salary = salary
    def give_raise(self, amount,bonus): #using a method from the parent class but adding more functionality. the method perameter changes here do not affect the parent class method 
        self.salary += amount + bonus 
        print(f"Congratulations Manager {self.name}! You raise is in the amount of ${amount}.00. Your bonus for this raise was {bonus}")

