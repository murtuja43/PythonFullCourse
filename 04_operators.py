#Arithmetic Operators (+  -  *  /)
#Python arithmetic operators perform basic mathematical operations on numeric data, such as addition, subtraction, multiplication, division, etc. Python arithmetic operators can be applied to various data types, including integers, floating-point numbers, and complex numbers.
a = 10
b = 5
print(a / b)


#Comparison Operators (==  !=  <  >  <=  >=)
#Comparison operators can be used to compare different values in Python, such as integers or strings.
a = 5<=3
print(a)


#Assignment Operatos (=  +=  -=)
#The simple assignment operator is the most commonly used operator in Python. It is used to assign a value to a variable. The syntax for the simple assignment operator is: variable = value. Here, the value on the right-hand side of the equals sign is assigned to the variable on the left-hand side.
a = 5
print(a)

b = 4
b -=2
print(b)



#Logical Operators (and, or, not)
#In Python, logical operators are used to combine multiple conditions together and evaluate them as a single boolean expression.

#and
a = True and False
b = False and True
c = False and False
d = True and True
print(a, b, c, d)
#we need both true statements to get the output True.

#or
a = True or False
b = False or True
c = True or True
d = False or False
print(a, b, c, d)
#we need at least one true statement to get the output True.


#not
a = not(True)
b = not(False)
print(a, b)
#this reverse the value.