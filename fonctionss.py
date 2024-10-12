def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)
 
 
print(f(3))



def fun(x):
    x += 1
    return x
 
 
x = 2
x = fun(x + 1)
print(x)



dictionary = {}
my_list = ['a', 'b', 'c', 'd']
 
for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )
 
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k.__getitem__(0), end=" ")
    
#print(dictionary)

def func_1(a):
    return a ** a
 
 
def func_2(a):
    return func_1(a) * func_1(a)
 
 
print(func_2(2))

def verify(a):
    if a is None:
        return False
    return True

a= None 
print(verify(a))

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return
 
 
print(fun(fun(2)))

def fun(x):
    global y
    y = x * x
    return y
 
 
fun(2)
print(y)

def any():
    print(var + 1, end='')
 
 
var = 1
any()
print(var)

my_tuple = (1, 2, 4, 8)
my_tuple2 = my_tuple[1] + my_tuple[0]

print(my_tuple2)


my_list = ['Mary', 'had', 'a', 'little', 'lamb']
 
 
def my_list1(my_list):
    del my_list[3]
    my_list[3] = 'ram'
 
 
print(my_list1(my_list))

def fun(x, y, z):
    return x + 2 * y + 3 * z
 
 
print(fun(0, z=1, y=3))

def fun(inp=2, out=3):
    print(inp ," ", out)
    return inp * out
 
 
print(fun(out=2))


dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)


tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)


try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")