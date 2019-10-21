# Summation of primes
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# 
# Sum of all primes under 2M is 142913828922
# --- 1548.936164855957 seconds ---

import time
start_time = time.time()

primes = [2, 3, 5, 7, 11, 13]

sumOfPrimes=sum(primes)

for num in range(14, 2000001):
    primeFound=True
    for prime in primes:
        if num%prime==0:
            primeFound=False
            break
    if primeFound:
        primes.append(num)
        sumOfPrimes += num

print('Sum of all primes under 2M is %d' %(sumOfPrimes))
print('--- %s seconds ---' % (time.time() - start_time))
