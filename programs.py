blocks = int(input("Enter the number of blocks: "))

for n in range(blocks): 
    if n*(n+1)/2 <= blocks: 
        height = n


print("The height of the pyramid:", height)


#### indicate year bissextile OR NOT 

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")

################

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

print ("\nList length:", len(numbers))  # Printing the list's length.

del  numbers[1]  # Removing the second element from the list.


numbers = [111, 7, 2, 1]
print(numbers[-1])  # Prints the last element of the list.


numbers  = [111, 7, 2, 1]
print(numbers[-2])  # Prints the second last element of the list.


#################


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
middle = int(input("Enter the number for replace "))
hat_list[2] = middle

print("replace list on middle ", hat_list)


del hat_list[-1]

print("delete last number ",hat_list)
# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print("lenght of list : ", len(hat_list))

print(hat_list)


#######

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

################

my_list = []  # Creating an empty list.

for i  in range(5):
    my_list.append(i + 1)

print(my_list)

#######

my_list = []  # Creating an empty list.
 
for i  in range(5):
    my_list.insert(0, i + 1)  # INVERSER
 
print(my_list)


##############

my_list = [10, 1, 8, 3, 5]
total = 0

for i  in range(len(my_list)):
    total += my_list[i]

print(total)


#######an other code 

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:  # same if using len(my_list)
    total += i
 
print(total)

###### Changement de valeurs

variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1

######### change value element list

my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)


# si nous devons parcourir plus de 100 elements

length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)