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