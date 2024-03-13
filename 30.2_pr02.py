class Calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        return (self.number)*(self.number)
    def cube(self):
        return (self.number)*(self.number)*(self.number)
    def squareroot(self):
        return pow(self.number,0.5)
    def printObj(self):
        print("The square of the number is:",self.square())
        print("The cube of the number is:",self.cube())
        print("The squareroot of the number is:",self.squareroot())

c=Calculator(3)
c.printObj()

    