#logic , number and text
#syntax: variable_name = variable_value

#no need to declare the type of each variable

#examples
number_of_days = 10

distance = 2.5

greeting = "Hello AI Viet Nam"

is_student = True

#type() function: return the type of a variable
a = 5
type_a = type(a)
print(type_a)

#rules: variables
#should have meaning
#cannot use keywords

#overflow and underflow
#1e = 10^

result = 1e-100
print(result)

result = 1e-1000
#this is underflow -> result would be 0.0

result = 1e1000
#this is overflow -> result would be inf

#string creation in Python
text1 = 'I love AI VietNam'

text2 = "I love AI VietNam"
