# Sum square difference

# The sum of the squares of the first ten natural numbers is,
#    1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# sum square difference 25164150
# --- 0.0020322799682617188 seconds ---

import time
start_time = time.time()

sumOfSquares=0
sum=0


for num in range(1, 101):
    sumOfSquares += num*num
    sum += num
    #print(num)

diff = sum*sum - sumOfSquares

print('Sum square difference %d' %(diff))
print('--- %s seconds ---' % (time.time() - start_time))
