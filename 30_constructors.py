class Employee:
    name="Harry"
    salary=900000
    center="Delhi"
    marks=34
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def printObj(self):#any other word can also be used instead of self
        print(f"The name is {self.name}")
        print(f"The marks are {self.marks}")
    
    
rohan=Employee("Rohan",100)
rohan.printObj()