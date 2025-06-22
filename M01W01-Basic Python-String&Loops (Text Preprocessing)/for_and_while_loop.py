#motivation
#repeat tasks

#for loop
for i in range(5): #0->4
    print('hello')

#default value
def add(a, b=10):
    return a+b

print(add(4))

#range(start=0, stop, step=1)
print(list(range(0,5,1))) #[0, 1, 2, 3, 4]

#break
for i in range(100):
    print(i)
    break #get out of for loop when i == 0

#continue: skip to the next loop
for i in range(5):
    if i == 3:
        continue
    print(i)
    #output: [0, 1, 2, 4]

