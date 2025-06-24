#compute sum
def compute_sum(data):
    res = 0
    for i in range(len(data)):
        res = res + data[i]
    return res

#sum of odd numbers
def compute_odd_sum(data):
    res = 0
    for item in data:
        if item%2 == 1:
            res = res + item
    return res

#linear searching
def linear_search(data, value):
    index = -1
    for i in range(len(data)):
        if data[i] == value:
            index = i
            break
    return index

#case study: list and integral
