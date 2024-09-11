my_list = [8, 10, 6, 2, 4]  # list to sort
 
for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.


print(my_list)

########### swapped option

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)


#### specific method sort in python

my_list = [8, 10, 6, 2, 4]  # list to sort
 
my_list.sort()  # sort() method sorts lists in ascending order by default.
 
print('Sorted list using sort method :', my_list)

## using reverse method

my_list = [8, 10, 6, 2, 4]  # list to sort
 
my_list.sort(reverse=True)  # sort() method sorts lists in ascending order by default.

 
#print('Sorted list using sort reverse :', my_list.reverse())
 
print('Sorted list using reverse method :', my_list)

lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)