#！/usr/bin/env python
#Collatz Returns!


#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz_steps(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            return  1 + collatz_steps(n/2)
        else:
            return 1 + collatz_steps(3*n+1)

#For example,

#print collatz_steps(1)
#>>> 0

#print collatz_steps(2)
#>>> 1

#print collatz_steps(6)
#>>> 8

#print collatz_steps(101)
#>>> 25
