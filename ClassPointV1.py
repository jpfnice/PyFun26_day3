"""
The class Point should offer:
    1 constructor
    2 attributes (x and y)
    1 operator: +
    2 methods: reset() and distance()
    
"""
import math

# __init__(), __new__(), __repr__(), __eq__() ... are predefined special methods
# automatically available. If needed you could redefine them ot add new methods
class Point: 
    def __init__(self, valx, valy):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y
    def reset(self):
        self.x=0
        self.y=0
    def distance(self, other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    
# center=Point(2,3)
# # 1) center=Point.__new__()
# # 2) center.__init__(2,3)
# # 3) __init__(center, 2, 3)

# print(center)
# # print(center.__repr__())

p1=Point(2,3) # a new point p1 is created with x=2 and y=3
# Point is a "constructor"
p2=Point(3,4)
print(p1) # <2,3>

p1.x=6 # to change the abcissa of p1. x is an "attribute"
p1.y=5

print(p1) # <6,5>
print(p2) # <3,4>

p3=p1+p2
# p3=p1.__add__(p2)
print(p3) # <9,9>

p1.reset()
print(p1) # <0,0>

result=p1.distance(p2)
print(f"The distance between {p1} and {p2} is {result}")
print(p2)
print(p3)
print("p2==p3",p2 == p3) # print("p2==p3",p2.__eq__(p3))
print(p2)
p3.x=3
p3.y=4
print(p3)
print("p2==p3",p2 == p3)



