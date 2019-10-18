# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Found Number 232792560
# --- 174.73073029518127 seconds ---

import time
start_time = time.time()

number = 2
while True:
    found=True
    for x in range(2, 20):
        if number%x!=0:
            found=False
            break
    if found:
        break
    number += 1

print("Found Number %d" %(number))
print("--- %s seconds ---" % (time.time() - start_time))
