# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math

num = 600851475143 
primes = [2, 3, 5, 7, 11, 13, 17]

largestPrime=-1

rangeUpper=math.ceil(math.sqrt(num))

for x in range(2, rangeUpper):
    #is x a factor of num?
    if num%x==0:
        #is x a prime
        primeNum=True
        for p in primes:
            if p > x:
                primeNum=False
                break
            if x%p==0:
                primeNum=False
                break
        if primeNum:
            largestPrime=x
            primes.append(x)


print('The largest prime number for %d is %d' %(num, largestPrime))
