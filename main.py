'''num = int(input())
def fib(a,b,c):
   if c == 1:
       print(a)
   else:
        print(a)
        z,a = a,a+b
        b = z
        return fib(a,b,c-1)

if num <= 0:
	print("Please enter a positive integer")
else:
	fib(0,1,num)


import numpy as np

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12]

array1 = np.asarray([list1,list2,list3])
print(array1)

array2 = np.transpose(array1)
print(array2)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

from itertools import chain, accumulate, takewhile
nums = list(accumulate(range(8)))
print (nums)

print(list(takewhile(lambda x: x<= 6, nums)))

from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(3 in num_set)
print("spam" not in word_set)

from itertools import count
for i in count(3):
    print(i)
    if i >=10:
        break'''





