list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

##########

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


#########

# Copying the entire list.
list_1 =  [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# negative index
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)


##########

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

#######

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

####### start

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

#####

my_list = [10, 8, 6, 4, 2]

new_list = my_list[:]
print(new_list)
# equivalent
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:len(my_list)]
print(new_list)

#######

my_list  = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


####### max in list

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

##### another program refactor max on list

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)


######### search element on list

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
found = False
x = 20

for i in my_list:
    if i == x:
        found = True
        break

print(found)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#remove duplicates
my_list = list(set(my_list))

print("The list with unique elements only:")
print(my_list)

######## another algo

# initializing list
my_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(my_list))

# using list comprehension + enumerate() to remove duplicated from list
res = [i for n, i in enumerate(my_list) if i not in my_list[:n]]

# printing list after removal
print ("The list after removing duplicates : "
        + str(res))

######## for comprehension list

# initializing list
my_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(my_list))

# using list comprehension to remove duplicated from list
res = []
[res.append(x) for x in my_list if x not in res]

# printing list after removal
print ("The list after removing duplicates : "
       + str(res))


######## list comprehension

squares = [x ** 2 for x in range(10)]
print("squares ",squares)

odds = [x for x in squares if x % 2 != 0 ]

print("odds ",odds)


# board = []
 
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

EMPTY=[]

board = [[EMPTY for i in range(8)] for j in range(8)]  # tableau à deux dimensions

print(board)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

times = [[0.0 for h in range(24)] for d in range(31)]

print(" times ", times)

print(" len ", len(times))

######### time manipulation

times = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#
 
total = 0.0
 
for day in times:
    total += day[11]
 
average = total / len(times)
 
print("Average temperature at noon:", average)


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True

print(" rooms ", rooms)

print("len rooms ", len(rooms))

# vacancy = 0
 
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1



# A four-column/four-row table ‒ a two dimensional array (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

x = 1
x = x == x
print(x)

i = 0
while i <= 3 :
    i += 2
    print("*")


i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

for i in range(1):
    print("#")
else:
    print("#")


print("Hachage #")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")


print("Hachage chevron")
var = 1
while var < 10:
    print("#")
    var = var << 1


print("evaluate condition")

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

a = 1
b = 0
c = a & b # 0
d = a | b # 1
e = a ^ b # 1
 
print(c + d + e)

my_list = [3, 1, -2]
print(my_list[-1])
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(nums)
print(vals)

print(len(nums))
print(len(vals))

nums = [1, 2, 3]
vals = nums[-1:-2]

print(nums)
print(vals)

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

my_list = [1, 2, 3]
print(len(my_list))
for v in range(len(my_list)):
    print(" value v = ",v)
    my_list.insert(1, my_list[v])
print(my_list)

my_list = [i for i in range(-1, 2)]
print(my_list)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
   
print(" tableau t ",t)
for i in range(3):
    s += t[i][i]
print(s)


# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")