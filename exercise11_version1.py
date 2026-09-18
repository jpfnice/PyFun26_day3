
"""
Class Stack definition:
    this version of Stack inherit from list
    
    Warning: 
    because it inherit from list, this version
    of Stack will have access to methods such as insert() or
    remove() ... normaly a Stack should not offer the 
    possibility to remove an element except 
    the last one or to insert an element elsewhere than at 
    the end
    Furthermore, the inherited method append(), will not
    take into account the Maximum Size of the stack
"""

class Stack(list):
    
    def __init__(self, maxSZ):
        if isinstance(maxSZ, int) and maxSZ > 0:
            self.maxSize=maxSZ
        else:
            print("Wrong size given, 10 used instead !")
            self.maxSize=10
        
    # NOT NEEDED ANYMORE: INHERITED FROM list
    # def __repr__(self):
    #     return f"({len(self.content)}/{self.maxSize}) {self.content}"
    
    # NOT NEEDED ANYMORE: INHERITED FROM list
    # def __len__(self):
    #     return len(self.content)
    
    # NOT NEEDED ANYMORE: INHERITED FROM list
    # def __eq__(self, other): # ==
    #     return self.maxSize == other.maxSize and self.content == other.content
    
    # NOT NEEDED ANYMORE: INHERITED FROM list
    # def __contains__(self, obj): # in operator
    #     return obj in self.content
    
    def push(self, obj):
        if len(self) >= self.maxSize: # if self.__len__() >= self.maxSize:
            print("Sorry: the stack is full!")
        else:
            self.append(obj)
    
    
    # WARNING: the new pop() methods needs to use 
    # the original pop() method, it does with the help of super()
    def pop(self):
        if len(self) <= 0:
            print("Sorry: the stack is empty!")
            return None
        else:
            #return self.pop(-1)
            return super().pop(-1) # To invoke the original version of pop()
        
    def peek(self):
        if len(self) <= 0:
            print("Sorry: the stack is empty!")
            return None
        else:
            return self[-1]
        
    def isEmpty(self):
        return len(self) == 0
        
s1=Stack(3) # A Stack with a maximum size of 10 elements
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
    
s2=Stack(20)
print(s1==s2) # Should print False
s2.push(20.3)
s2.push(3.5)
print(s1==s2) # Should print True

if 3.5 in s2: # if s2.__contains__(3.5):
    print("3.5 is present")
    
for elt in s2:
    print(elt)
    