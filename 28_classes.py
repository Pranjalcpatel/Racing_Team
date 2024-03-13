class Employee:
    name="Harry"
    salary=900000
    center="Delhi"
    def printObj(self):#any other word can also be used instead of self
        print(f"The name is {self.name}")
        print(f"The salary is {self.salary}")
        


harry=Employee() #initialising a variable of class employee
harry.marks=23 #setting instance attributes
Employee.marks=100 #setting class attributes


harry.printObj()
Employee.printObj(harry)
#both give same output



