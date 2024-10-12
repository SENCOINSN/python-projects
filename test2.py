my_list = [1, 2]
 
for v in range(2):
    my_list.insert(-1, my_list[v])
 
print(my_list)

nums = [1, 2, 3]
vals = nums[:-1]

print(nums)
print(vals)

print(1//2)

def func(a, b):
    return b ** a
 
 
print(func(b=2, a=3))

z = 0
y = 10
x = y < z and z > y or y < z and z < y

print(x)


my_list = [x * x for x in range(5)]
 
 
def fun(lst):
    print("initial list ",lst)
    print("remove element at index 2 ",lst[lst[2]])
    del lst[lst[2]]
    return lst
 
 
print(fun(my_list))

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
 
print(x, y, z)


a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
 
print(a, b)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
 
 
print(fun(fun(2)))

nums = [1, 2, 3]
vals = nums
del vals[:]
print(vals)
print(nums)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# y = input()
# x = input()
# print(x + y)

print("a", "b", "c", sep="sep")

x = 1 // 5 + 1 / 5
print(x)

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
 
for k in range(len(dct)):
    v = dct[v]
 
print(v)

lst = [i for i in range(-2, -1)]
print(lst)

def fun(a, b, c=0):
    print(a, b, c)
    
fun(0,1,2)
fun(b=0, a=2)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
 
 
print(fun(0, 3))

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)


# dd = {"1": "0", "0": "1"}
# for x in dd.values():
#     print(x, end="")
    
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

print(dct)
 
# for x in dct.keys():
#      print(dct[x][1], end="")
 
 
lst = [[x for x in range(3)] for y in range(3)]
 
for r in range(3):
    for c in range(3):
        #print(lst[r][c] % 2 != 0)
        if lst[r][c] % 2 != 0:
            print("#")
            

foo = (1, 2, 3)
print(foo[0])
    