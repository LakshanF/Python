# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# 906609 is a palindrome
# --- 0.9486141204833984 seconds ---

import time
start_time = time.time()

largestPalNum=1

for n1 in range(999,1,-1):
    for n2 in range(999,1,-1):
        number = n1*n2
        numStr = str(number)
        i=0
        j=len(numStr)-1

        isPalindrome = True
        while(i<j):
            if numStr[i]!=numStr[j]:
                isPalindrome=False
                break
            i +=1
            j -=1
        if isPalindrome:
            if number > largestPalNum:
                largestPalNum = number

print('%d is a palindrome' %(largestPalNum))
print("--- %s seconds ---" % (time.time() - start_time))
