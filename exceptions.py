# x = int(input("Enter an integer: "))

# if type(x) is not int:  # using type to verify is int
#     raise TypeError("Only integers are allowed")

# try: 
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)        
# except ValueError:
#     print('I do not know what to do.')    
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.') 


# default exception

try:  
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
    
    

while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
        


while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")
        

# enhanced exception

try:  
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except (ValueError, ZeroDivisionError):
    print('I do not know what to do.')