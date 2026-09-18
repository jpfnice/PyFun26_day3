
# l1=[5,6,5,6,8,7,5,10,20]
# print(l1)
# l1.remove(5)
# print(l1)

class ListPlus(list):
    def removeAll(self, obj):
        while obj in self:
            self.remove(obj)
    def __add__(self, other):
        newList=[]
        if len(self) > len(other):
            for index in range(len(other)): 
                newList.append(self[index]+other[index])
            for index in range(len(other), len(other)): 
                newList.append(self[index])
        else:
            for index in range(len(self)):
                newList.append(self[index]+other[index])
            for index in range(len(self), len(other)):
                newList.append(other[index])    
        return newList

l1=ListPlus()
l1.append(12)
l1.insert(0,12)
l1.append(13)
l1.append(14)
l1.append(12)
print(l1)
l2=ListPlus([6,7,8])
print(l2)
l1.removeAll(12)
print(l1)
l3=l1+l2 # l3=l1.__add__(l2)
print(l3)