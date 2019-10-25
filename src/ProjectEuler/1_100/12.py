# Highly divisible triangular number
# 
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# 
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?
# 
# 76576500
# strategy
# - brute force: go from the beginning and figuring out the factors till they reach 500
#   * forced stop after 3 hours on my Z240 powerstation :-(
# - start from 500th triangle number, use smart strategies (multiple of small primes)
# 
#

import math
import time
start_time = time.time()

def brute_force():
    number = 2
    while True:
        sum=0
        for n in range(1, number+1):
            sum += n
        factors = [1, sum]
        for factor in range(2, math.floor(sum/2) + 1):
            if sum%factor == 0:
                factors.append(factor)
        if len(factors) > 500:
            print('%d triangle number is %d and has %d factors' %(number, sum, len(factors)))
            break
        number += 1

# will first create a number of primes and then do a smarter factoring
def smart_factoring():
    #get primes
    primeSleeve = [True]*10000
    numPrimes=0
    primes = []
    firstIndex=0
    while numPrimes < 10:
        firstIndex = primeSleeve.index(True, firstIndex) 
        prime = firstIndex + 2
        numPrimes += 1
        primes.append(prime)
        index = firstIndex
        while index < (len(primeSleeve) - prime - 1):
            index += prime
            primeSleeve[index] = False
        firstIndex += 1
    
    triangleNum=1
    increment=1
    numberOfFactors=1
    while numberOfFactors < 6:
        increment +=1
        triangleNum += increment
        factors = [1, triangleNum]
        for p in primes:
            if p > triangleNum:
                break
            pm=p
            while triangleNum%pm==0:
                if not pm in factors:
                    factors.append(pm)
                pm +=p
        numberOfFactors = len(factors)
    return triangleNum




#brute_force()
retValue = smart_factoring()
print(retValue)

print('--- %s seconds ---' % (time.time() - start_time))
