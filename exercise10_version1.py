
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
class Stack:
    
    def __init__(self,maxSZ):
        if isinstance(maxSZ, int) and maxSZ> 0:
            self.maxSize=maxSZ
        else:
            print("Wrong size given, 10 used instead !")
            self.maxSize=10
        self.content=[]
        
    def __repr__(self):
        return f"({len(self.content)}/{self.maxSize}) {self.content}"
    
    def __len__(self):
        return len(self.content)
    
    def __eq__(self, other):
        return self.maxSize == other.maxSize and self.content == other.content
    
    def push(self, obj):
        if len(self) >= self.maxSize:
            print("Sorry: the stack is full!")
        else:
            self.content.append(obj)
            
    def pop(self):
        if len(self) <= 0:
            print("Sorry: the stack is empty!")
            return None
        else:
            return self.content.pop(-1)
        
    def peek(self):
        if len(self) <= 0:
            print("Sorry: the stack is empty!")
            return None
        else:
            return self.content[-1]
        
    def isEmpty(self):
        return len(self) == 0
        
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