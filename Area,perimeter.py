class Rectangle():
    def __init__(self,Area,Perimeter):
        self.Area=Area
        self.Perimeter=Perimeter
    def area(self):
         return self.Area * self.Perimeter
    def perimeter(self):
        return 2 * (self.Area + self.Perimeter)
A=Rectangle(2,5)
print("Area=",A.area())
print("Perimeter=",A.perimeter())