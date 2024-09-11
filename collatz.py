def collatz(n):
    step=0
    while n > 1:
        #print(n, end=' ')
        if (n % 2) != 0:
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
        step +=1
        print(n, end='\n')
    #print(1, end='')
    print(" steps = ",step)
 
 
n = int(input('Enter n: '))
print('Sequence: ', end='\n')
collatz(n)
