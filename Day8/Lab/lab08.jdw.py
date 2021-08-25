## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


## Def: Let x, y be nonzero integers

def gcd(x, y):
    if y > x:
        a,b = y,x
    else:
        a,b = x,y
    r = a % b
    if r == 0:
        return b
    else: 
        return gcd(b, r)

# Test:
gcd(10, 21)
gcd(11, 22)

gcd(125, 500)
gcd(270, 192)
gcd(2, 999)


## Problem 2
## Write a function using recursion that returns prime numbers less than 121
## remember, primes are not the product of 
## any two numbers except 1 and the number itself
## hint, "hardcode" 2
import math

def find_primes(n, primes = []):    
    if n == 2:
        primes.append(2)
        return primes    
    
    flag = True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % 1 == 0:
            flag = False
            break
    if flag:
        primes.append(n)
        
    return find_primes(n - 1, primes)

find_primes(121)

## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

def T(n, from_rod, to_rod, mid_rod):
    # Base case: n = 1
    if n == 1:
        print("Move Disk 1 from {} to {}.".format(from_rod, to_rod))
    else:
        T(n-1, from_rod, mid_rod, to_rod)
        print("Move disk {} from {} to {}.".format(n, from_rod, to_rod)
    
    return T(n-1, mid_rod, to_rod, from_rod)



T(1, "A", "C", "B")
T(2, "A", "C", "B")
T(3, "A", "C", "B")

