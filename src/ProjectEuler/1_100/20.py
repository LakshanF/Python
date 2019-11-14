# Factorial digit sum
# 
# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!
# 
# Sum of the digits for 100 is 648
# --- 0.0009698867797851562 seconds ---

import time
start_time = time.time()

n = 100
total=1
for number in range(1, n+1):
    total *= number

#@TODO - can this be done via list expression?
digitSum=0
for c in str(total):
    digitSum += int(c)

print('Sum of the digits for %d is %d' %(n, digitSum))
print('--- %s seconds ---' % (time.time() - start_time))
