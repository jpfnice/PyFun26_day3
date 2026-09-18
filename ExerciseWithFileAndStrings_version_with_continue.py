"""  
Given a file with this format (you can use "data.txt" for instance or create your own test file):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.

To extract the 2 float out of each line you could:
    1) use slices
    2) use 2 split() methods
    3) use another strategy ??
    
Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

"""

import math

datafile=open("data.txt")

X1=[]
X2=[]

for line in datafile:
    # a line do have the following format:
    #  "    x1:0.34;x2:0.56\n"
    
    result=line.split(";")
    
    if len(result) != 2:
        print(line, "does not have the expected format!")
        continue
    values=result[0].split(":")
    if len(values) != 2:
        print(line, "does not have the expected format!")
        continue
    # values is a list like that: ["   x1", "0.34"]
    X1.append(float(values[1]))
    values=result[1].split(":")
    if len(values) != 2:
        print(line, "does not have the expected format!")
        continue
    # values is a list like that: ["x2", "0.56\n"]
    X2.append(float(values[1]))   

datafile.close()

print(X1)
print(X2)

Y1=[]
Y2=[]

# The following code will only work if the 2 list X1 and X2 are 
# of the same size:
# for index in range(len(X1)): # index will vary from 0 to 33
#     Y1.append(math.cos(X1[index]))
#     Y2.append(math.sin(X2[index]))

for e in X1:
    Y1.append(math.cos(e))

for e in X2:
    Y2.append(math.sin(e))
    
print(Y1)
print(Y2)
    
