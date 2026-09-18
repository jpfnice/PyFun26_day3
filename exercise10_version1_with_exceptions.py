
class StackError(Exception):
    pass
class StackSizeError(StackError):
    pass
class StackFullError(StackError):
    pass
class StackEmptyError(StackError):
    pass

class Stack:
    def __init__(self, maxSZ):
        if isinstance(maxSZ, int) and maxSZ > 0:
            self.maxSize=maxSZ
        else:
            raise StackSizeError(f"Wrong size given: {maxSZ} !")
            # self.maxSize=10 # => NOT NEEDED, the raise statements makes python leave
            # __init__()
        self.content=[]
        
    def __repr__(self):
        return f"({len(self.content)}/{self.maxSize}) {self.content}"
    
    def __len__(self):
        return len(self.content)
    
    def __eq__(self, other): # ==
        return self.maxSize == other.maxSize and self.content == other.content
    
    def __contains__(self, obj): # in operator
        return obj in self.content
    
    def push(self, obj):
        if len(self) >= self.maxSize: # if self.__len__() >= self.maxSize:
            raise StackFullError("Sorry: the stack is full!")
        else:
            self.content.append(obj)
            
    def pop(self):
        if len(self) <= 0:
            raise StackEmptyError("Sorry: the stack is empty!")
            # return None # => NOT NEEDED, the raise statements makes python leave
            # pop()
        else:
            return self.content.pop(-1)
        
    def peek(self):
        if len(self) <= 0:
            raise StackEmptyError("Sorry: the stack is empty!")
        else:
            return self.content[-1]
        
    def isEmpty(self):
        return len(self) == 0

try:    
    s1=Stack(20) # A Stack with a maximum size of 10 elements

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
    
    if 3.5 in s2: # if s2.__contains__(3.5):
        print("3.5 is present")
        
    for elt in s2:
        print(elt)
except StackError as ex: # to handle all kinds of StackErrors
    print("Exception:", ex)
    
# You can also handle separatly: StackFullError, StackEmptyError, etc ...