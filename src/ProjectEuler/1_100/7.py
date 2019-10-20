# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 10001 prime is 104743
# --- 6.776766061782837 seconds ---

import time
start_time = time.time()


primes = [2, 3, 5, 7, 11, 13]

number = 14
primeNumbers=len(primes)

while primeNumbers < 10001:
    primeFound=True
    for prime in primes:
        if number%prime == 0:
            primeFound = False
            break
    if primeFound:
        primeNumbers += 1
        primes.append(number)
    number += 1

print('10001 prime is %d' %(number-1))
print('--- %s seconds ---' % (time.time() - start_time))
