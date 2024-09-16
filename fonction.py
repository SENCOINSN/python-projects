def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


adding(1, 2, 3)

#adding(1,a=2,b=3)

def introduction1(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction1()

def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(5, 2) # Syntax Error

def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")


def add_numbers(a, b=2, c=0): #(a,b=2,c)  #Erreur de syntaxe- un argument non par défaut (c) suit un argument par défaut (b=2).
    print(a + b + c)
 
add_numbers(a=1, c=3) 


def  strange_function(n):
    if(n % 2 == 0):
        return True
    

print(strange_function(2))
print(strange_function(3))

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s


print(list_sum([1, 2, 3, 4, 5]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))



def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))

###########

def is_prime(num):
    print("number : ", num,  " number sqrt : ",int(1 + num ** 0.5)) 
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


def my_function():
    var = 2
    print("Do I know that variable?", var)
 
 
var = 1
my_function()
print(var)

# le var la variable créée à l’intérieur de la fonction n’est pas la même que lorsqu’elle est définie à l’extérieur de celle-ci ‒ il semble qu’il y ait deux variables différentes du même nom ;
# de plus, la variable de la fonction fait de l'ombre à la variable provenant du monde extérieur.


def  my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1 
my_function()
print(var)


def  my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1 # l'argument de la fonction n'est pas la même que lorsqu'elle est définie à l'extérieur de celle-ci.
        # la valeur de l'argument est donnée à la fonction, et non l'argument lui meme. C'est un passage par valeur
my_function(var)
print(var)


def rotation(a, b):  # passage par valeur et non par reference
    z=a 
    a=b
    b=z
    print("a = ", a, "b = ", b)


a = 1
b = 2

rotation(a, b)

print("a = ", a, "b = ", b)


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)  # my_list_1 and my_list_2 are passed by reference to the function. la liste est modifiée à ce niveau
print("Print #5:", my_list_2)



var = 2
print(var) # outputs: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # outputs: 5
print(var) # outputs: 5


# IMC function with default value

def bmi(weight, height):
    return weight / height ** 2
 
 
print(bmi(52.5, 1.65))

def  bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))


# convert feet and inches to meters

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


def  is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


#more compact

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
 

 # Trouver l'aire du triangle en utilisant la formule de Heron

def heron(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(heron(1., 1., 2. ** .5))


# Factorielle

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # testing
    print(n, factorial_function(n))



#fibonacci

def fibonacci(n):
    if n < 0:
        return None
    if n < 3:
        return n
    a, b = 1, 1
    for i in range(3, n + 1):
        print("a = {}, b = {}".format(a, b))
        a, b = b, a + b
    return b

for i in range(1, 10):
    print(i, fibonacci(i))



# exemple fonction recursive fibonacci

def fibonacci(n):
    if n < 0:
        return None
    if n < 3:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 10):
    print(i, fibonacci(i))


# recursive factorial

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    return n * factorial_function(n - 1)
 
for n in range(1, 6): # testing
    print(n,"! : ", factorial_function(n),end="\n")


def fun(a):
    if a > 30:
        return 3
    else:
        print(" a evaluate ", a+3)
        return a + fun(a + 3)
 
 
print(fun(25))