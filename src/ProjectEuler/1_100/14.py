# Longest Collatz sequence
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 
# longest collatz number 837799 with chain 525
# --- 55.672569036483765 seconds ---

import time
start_time = time.time()

longestChain=0
collatzNum=0
for num in range(2,1000001):
    n=num
    chain=1
    while n > 1:
        if n%2==0:
            n = (int)(n/2)
        else:
            n = 3*n + 1
        chain +=1
    if chain > longestChain:
        longestChain = chain
        collatzNum = num

print('longest collatz number %d with chain %d' %(collatzNum, longestChain))
print('--- %s seconds ---' % (time.time() - start_time))
