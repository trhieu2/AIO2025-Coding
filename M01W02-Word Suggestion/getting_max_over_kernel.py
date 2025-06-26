def getting_max_over_kernel(data, k):
    if k == 1:
        return data

    else:
        result = []
        i = 0
        j = k
        while(j<=len(data)):
            temp = data[i:j]
            temp.sort()
            result.append(temp[-1])
            i = i+1
            j = j+1

    return result

data = [3,4,5,1,-44,5,10,12,33,1]

print(getting_max_over_kernel(data, 3))

#can also implement using max function
def getting_max_over_kernel_v2(data, k):
    result = []
    temp = []

    for el in data:
        temp.append(el)

        if len(result) == k:
            result.append(max(temp))
            del temp[0]

    return result