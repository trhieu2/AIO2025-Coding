#pi estimation
n = 10000
pi = 0
for i in range(1, n+1):
    pi = pi + (((-1)**(i+1))/(2*i-1))
print(pi*4)

#compute quadratic root for the number N
def compute_square_root(a, n):

    '''
    This function aims to compute the square root for the number n
    :param a: the number needs to take square root
    :param n: the number of loops for optimization
    :return: square root value of the number
    '''

    result = a/2

    for _ in range(n+1):
        result = (result + result/2)/2

    return result

#compute the area of a unit circle
import math
def compute_y(x):
    return math.sqrt(1-x*x)

length = 2
delta = 0.0001

x = -1
area = 0
for _ in range(int(length/delta)):
    area = area + delta*compute_y(x)

    x = x + delta

print(area*2)