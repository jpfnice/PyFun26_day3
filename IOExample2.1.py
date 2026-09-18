
with open("data.txt") as myfile:
    value=myfile.readline() # to read the first line
    print(value)
    value=myfile.readline() # to read the second line
    print(value)
    value=myfile.readlines() # To read the remaining lines (a list of lines)
    print(value)
    
print("The end")