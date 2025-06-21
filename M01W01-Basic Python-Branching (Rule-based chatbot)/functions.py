#motivation: repeat a task/separate a task
#input: what the function needs to do a task
#output: what comes out of the function

#built-in functions
a = 5
print(a)
type(a)

#random and math modules
#absolute value of x
import math

n1 = 1
n2 = 2
print(math.fabs(n1))

#generate a random number in python
import random

rand_num = random.random()
print(rand_num)

#compute square root
num = 16
sq_root = math.sqrt(num)
print(sq_root)

#exponential of x
x = 2
print(math.exp(x))

#log(x)
#log() function properties: monotonic:f(x1) < f(x2) (in cases when we only care about the right one, not its value, or the maximum/minimum),
x = 4
print(math.log(x))
print(math.log(math.e))

#design a loss function: application of log function
#we have 9 red balls, 1 blue ball
#A: get a red ball -> p(A) = 0.9
#B: get a blue ball -> p(B) = 0.1
#E: pick a ball from the basket
#how to measure the surprises ?
#observation surprise(E) >< p(E) ->surprise(E) = 1/p(E)
#problem surprise(E) in [1, +inf)
#log(surprise(E)) = log(1/p(E)) = -log(p(E)) in [0, inf)
#In information theory: Information(x) = -log(p(x))


#logarithm and small numbers: to preserve the relative order
v1 = 0.0004
v2 = 0.0003
v = v1*v2 #too small

v = math.log(v1) + math.log(v2) #avoid underflow


#exponential function: x in (-inf, inf), f(x) in [0, inf)
num1 = 2
num2 = 5
num3 = 3

#compute total
total = num1 + num2 + num3

#compute percentage
per1 = num1/total
per2 = num2/total
per3 = num3/total

#assumption: xi >= 0
#problem: compute the percentage of <0 value -> use exponential func -> softmax

num1 = 1.0
num2 = 3.0

exp_num1 = math.exp(num1)
exp_num2 = math.exp(num2)
total = exp_num1 + exp_num2

per1 = exp_num1/total
print(per1)
per2 = exp_num2/total
print(per2)


#USER-DEFINED FUNCTIONS
#define func name: lowercase with underscore and begin with a verb
#identation: use 4 spaces
#determine function parameters: input data help the function done
#do docstring: explain and describe the function

def compute_salary(salary):
    '''
    This function aims to compute the increased salary of a person
    :param salary: current salary
    :return: new salary
    '''
    return salary + 1

#convert degree to radian using math.radians
#compute the area of a unit circle
def estimate_area(alpha):
    radians = math.radians(alpha)

    sin_alpha = math.sin(radians)
    cos_alpha = math.cos(radians)

    area_alpha = (sin_alpha*cos_alpha)/2
    return (area_alpha*(360/alpha))  


