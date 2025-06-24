#From 1D to 2D List (Review)
student_list = ['vinh', 'an', 'toan', 'lam', 'tam', 'chuyen']
row_class = 3
col_class = 2
def find_student(student, r, c):
    index = (r-1)*col_class + (c-1)
    return student[index]

print(find_student(student_list, 3, 1))

#-------------------------------------------------------
row1_stud = ['vinh', 'an']
row2_stud = ['toan', 'lam']
row3_stud = ['tam', 'chuyen']

student_lst = [row1_stud, row2_stud, row3_stud] #2D List

def find_stu(student, r, c):
    return student[r-1][c-1]

print(student_lst[2][0])

#TUPLE - Immutable List
x = ('glem', 'sally', 'joseph')
print(x[2])
print(x)
print(max(x))

#tuple unpacking
x1, y1, z1 = ('a', 'b', 'c')
(x2, y2, z2) = ('a', 'b', 'c')

print(x1)
print(x2)

#() can be removed when tuple is initiated

#tuple with one element
var3 = (1,)
print(type(var3))

data = (1,2,3,4,5)
print(data[2:])
print(data[::-1]) #output: [5,4,3,2,1]

#SET - unique List - unordered - can store different types of variables
animals = {"cat", "dog", "tiger"}
#access items
for animal in animals:
    print(animal)

#copy
a_copy = animals.copy()

#add an item
animals.add("bear")

#join two sets
set1 = {'cat', 'dog'}
set2 = {'duck', 'bird'}

set3 = set.union(set1, set2)

#inset a set into another set
animals.update({"chicken", "duck"})

#difference
set1 = {'apple', 'banana', 'cherry'}
set2 = {'pinapple', 'apple'}

set3 = set1.difference(set2)
print(set3)

set1.difference_update(set2)
print(set1)

set4 = set1.symmetric_difference(set2)

#bitwise operator
#&: and, |: or, ^: xor(symmetric diff), -:difference

#remove an item - can raise an error if not existing
animals.remove('dog')

#discard an item - remove if exists
animals.discard('tiger')

#---------------------------------------------------------------
#DICTIONARY
#Any immutable can be Dictionary key
parameters = {'learning rate':0.1, 'optimizer':'Adam','metric':'Accuracy'}

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

#copy() is shallow copy
#copy.deepcopy() is deep copy

#get keys and values
keys = parameters.keys()
for key in keys:
    print(key)

values = parameters.values()
for value in values:
    print(value)

items = parameters.items()
for key, value in items:
    print(key, value)

value = parameters.get('learning rate')
print(value)

value = parameters.pop('learning rate')
#After using pop() func: {'optimizer':'Adam', 'metric':'Accuracy'}

