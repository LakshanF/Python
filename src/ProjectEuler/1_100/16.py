# Power digit sum
# 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
# 
# The sum is 1366
# --- 0.0009722709655761719 seconds ---

import math
import time
start_time = time.time()

num=1

for pow in range(1, 1001):
    num += num

sum=0
origNum=num
while num>0:
    sum += num%10
    num //= 10

print('The sum is %d' %(sum))

print('--- %s seconds ---' % (time.time() - start_time))
