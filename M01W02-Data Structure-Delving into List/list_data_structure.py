#list is the most important data structure to learn
#list>dict>tuple>set>....
a_lst = [0, 6, 4]
print(a_lst)

#empty list
emp_lst = []

#different types of data
var_lst = [1, 'hello'] #not frequently used

#list is 0-indexed
print(a_lst[0])

print(a_lst[5]) #out of bound -> error

#should only focus on forward index
#quick access the last element
print(a_lst[-1])

#slicing
#syntax list[start:end:step]
print(a_lst[0:3]) # 0, 1, 2

#get the number of elements of a list
len(a_lst)

#+ and * operators
data1 = [6, 5, 7]
data2 = [1, 2, 3]

data3 = data1 + data2

_lst = [None]*10

#add an element
data1.append(4) #add 4 to the end of the list

data1.insert(1,9) #[0, 9, 6, 4]

def my_insert(data, index, value):
    result = data[:index] + value + data[index:]

    return result

def my_insert_2(data, index, value):
    result = []

    for i in range(len(data)):
        if i == index:
            result.append(value)
            result.append(data[i])
        else:
            result.append(data[i])

    return result

#extend at the end
data1.extend([9, 2])

#sort() function
data1.sort() #ascending order

#delete an element
data1.pop(-1) #delete at index -1

data1.remove(5) #delete the first element with the value 5
#if not exist -> error

def count(value, data):
    result = 0
    for i in range(len(data)):
        if data[i] == value:
            result = result + 1
    return result

del data1[1:3] #delete from ele 1->2

#index() function -> return the first element with the given value
data =[1,7,4,7,2]

for item in data:
    if item == 7:
        print('found')
        break

for i in range(len(data)):
    if data[i] == 7:
        print('found', i)
        break

#reverse() function

#count() function
data.count(7) #returns the number of element with the value 7

#copy() function
data = [1,2]
data2 = data.copy()

data2[0] = 9 #data[0] is still 1

#zip() function
scores = [1,2,7,4]
names=['john', 'peter', 'mary', 'smith']

for score, name in zip(scores, names):
    print(score, name)

#enumerate
for i, name in enumerate(names):
    print(i, name)

#2D LIST
data = [[0,1,2],[3,4,5]]

def print_matrix(data, num_rows, num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            print(data[i][j], end =' ')
        print()



