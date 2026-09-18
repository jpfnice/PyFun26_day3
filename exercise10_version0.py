
"""
Class Stack definition:
    Attributes:
        maxSize (an int)
        content (a list)
    Methods:
        __init__()
        push()
        __repr__()
        __len__()
        pop()
        peek()
        isEmpty()
        __eq__()

"""

s1=Stack(10) # A Stack with a maximum size of 10 elements
s1.push(20.3)
s1.push(3.5)
s1.push(4.5)
print("S1 is", s1) # S1 is (3/10) [20.3, 3.5, 4.5]

print("Current size of s1 is", len(s1)) # Current size of s1 is 3
top=s1.pop()
print(top) # 4.5
print("Current size of s1 is", len(s1)) # Current size of s1 is 2
top=s1.peek()
print(top) # 3.5
print("Current size of s1 is", len(s1)) # Current size of s1 is 2
print("S1 is", s1)# S1 is (2/10) [20.3, 3.5]
if s1.isEmpty():
    print("S1 is empty")
else:
    print("S1 is not empty")
    
s2=Stack(10)
print(s1==s2) # Should print False
s2.push(20.3)
s2.push(3.5)
print(s1==s2) # Should print True