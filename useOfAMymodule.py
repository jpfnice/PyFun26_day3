# Version 1
# import mymodule

# # mymodule.py mymodule.pyc mymodule.pyo
# # import sys
# # print(sys.path)

# s1=mymodule.Stack(10)
# print(s1)

# Version 2
# import mymodule as my

# # mymodule.py mymodule.pyc mymodule.pyo
# # import sys
# # print(sys.path)

# s1=my.Stack(10)
# print(s1)

# Version 3
from mymodule import Stack, StackError

# mymodule.py mymodule.pyc mymodule.pyo
# import sys
# print(sys.path)

s1=Stack(10)
print(s1)