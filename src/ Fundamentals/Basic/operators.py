'''
Author: Tiago Gomes
Data: 16/11/2024
Version: 1.0
'''

'''
Operator	Name	                    Example	Try it
    ==	    Equal	                        x == y	
    !=	    Not equal	                    x != y	
    >	    Greater than	                x > y	
    <	    Less than	                    x < y	
    >=	    Greater than or equal to	    x >= y	
    <=	    Less than or equal to	        x <= y
'''

ex0 = 'car' == 'car'
print(ex0)

ex1 = 'glasses' == 'Glasses'  # Case sensite
print(ex1)

ex2 = 'glasses' != 'Glasses'
print(ex2)

ex3 = 10 > 8
print(ex3)

ex4 = 3 > 8
print(ex4)

ex5 = 3 >= 3
print(ex5)

'''
Logical operators are used to combine conditional statements:

Operator	                        Description	                                                            Example
    and 	        Returns True if both statements are true	                    x < 5 and  x < 10	
    or	            Returns True if one of the statements is true                   x < 5 or x < 4	
    not	            Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
'''

ex6 = 5
print(ex6 > 3 and ex6 < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

ex7 = 5
print(ex7 > 3 or ex7 < 4)
# returns True because one of the conditions are true
# (5 is greater than 3, but 5 is not less than 4)

ex8 = 5
print(not (ex8 > 3 and ex8 < 10))
# returns False because not is used to reverse the result

'''
Python Identity Operators

Operator	Description	                                                    Example
is 	            Returns True if both variables are the same object	         x is y	
is not	        Returns True if both variables are not the same object	x    is not y
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


'''
Python Membership Operators

Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
'''
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
