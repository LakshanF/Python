# Special Pythagorean triplet
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
#           a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 
# 31875000
#
# a * b * c = 31875000
# --- 0.07599973678588867 seconds ---


import time
start_time = time.time()

num=0

for a in range(1,998):
    numFound=False
    for b in range(1, 998):
        if b <= a:
            continue
        c = 1000 - a - b
        if c <= b:
            continue
        if c*c == (a*a + b*b):
            numFound = True
            num = a*b*c
            print('a - %d, b - %d, c - %d' %(a, b, c))
            break
    if numFound:
        break

print('a * b * c = %d' %(num))
print('--- %s seconds ---' % (time.time() - start_time))
