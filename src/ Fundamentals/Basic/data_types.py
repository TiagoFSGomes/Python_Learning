'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

'''
Example	                                             Data Type	
x = "Hello World"	                                    str	
x = 20	                                                int	
x = 20.5	                                            float	
x = 1j	                                                complex	
x = ["apple", "banana", "cherry"]	                    list	
x = ("apple", "banana", "cherry")	                    tuple	
x = range(6)	                                        range	
x = {"name" : "John", "age" : 36}	                    dict	
x = {"apple", "banana", "cherry"}	                    set	
x = frozenset({"apple", "banana", "cherry"})	        frozenset	
x = True	                                            bool	
x = b"Hello"	                                        bytes	
x = bytearray(5)	                                    bytearray	
x = memoryview(bytes(5))	                            memoryview	
x = None                                                NoneType

'''

# list
l = ['apple', 'banana', 'cherry']
# display list:
print(l)
# display the data type of list:
print(type(l))

# tuple
t = ('apple', 'banana', 'cherry')
# display t:
print(t)
# display the data type of tuple:
print(type(t))

# Range
r = range(6)
# display range:
print(r)
# display the data type of range:
print(type(r))

# Dict
d = {'name': 'John', 'age': 36}
# display dict:
print(d)
# display the data type of dict:
print(type(d))

# Set
s = {'apple', 'banana', 'cherry'}
# display set:
print(s)
# display the data type of set:
print(type(s))

# None
n = None
# display none:
print(n)
# display the data type of none:
print(type(n))
