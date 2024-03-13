class Employee:
    name="Harry"
    salary=900000
    center="Delhi"
    @staticmethod #doesn't need to access the class's attributes
    def greet():#no self word required
        print("Hello!!")
    def printObj(self):#any other word can also be used instead of self
        print(f"The name is {self.name}")
        print(f"The salary is {self.salary}")


harry=Employee()
harry.greet()
Employee.greet()