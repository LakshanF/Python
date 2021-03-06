# Largest product in a series
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# 
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
# 
# LEARNINGS
#   - Python seems to manage its number types, int and long in a transparent way.
#   - The first approach of digit manipulation didnt work
#       * sum = Get the initial value of multiplying the first 13 characters converted to int
#       * from index: 14th position to 1000th
#           * divide sum with (index-13)th digit (if 0, set sum to 1)
#           * multiply with the index digit
#           * if new value > previous
#               * set max to new value
#   - Didnt fully debug but likely an issue with data type conversion when sum is divided by int (double)
#
# Largest product in a series is 23514624000
# --- 0.00700068473815918 seconds ---

import time
start_time = time.time()

allDigits=''
f = open('./src/ProjectEuler/1_100/8.txt', 'r')
for x in f:
    allDigits += ''.join(i for i in x if i.isdigit())

maxSumValue=0
for i in range(0, 988):
    sum=1
    for c in allDigits[i:i+13]:
        sum *= int(c)
    if sum > maxSumValue:
        maxSumValue = sum

print('Largest product in a series is %d' %(maxSumValue))
print('--- %s seconds ---' % (time.time() - start_time))


