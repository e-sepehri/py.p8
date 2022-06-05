# Class
#Q9 <<
'''
class Circle:
    def __init__(self, r):
        self.radius = r

    def perimeter(self):   #computes perimeter(mohit)
        return 2 * 3.14 * self.radius
        
    def area(self):        #computes area(masahat)
        return 3.14 * self.radius**2

My_circle = Circle(int(input('Enter number as radius: ')))
print("Area of circle :", My_circle.area())
print("Perimeter of circle :", My_circle.perimeter())
'''
#Q11 <<
''' a) 40  0  41  1  50  21
    b) 0
    c) if the given number is less than 40 it would return 0 But if \
       the given number >= 40 would return itself So the user determines.'''