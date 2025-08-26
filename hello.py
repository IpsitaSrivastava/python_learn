year = input()
def is_leap(year):
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap(year))

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = [[i, j, k] 
                   for i in range(x+1) 
                   for j in range(y+1) 
                   for k in range(z+1) 
                   if (i + j + k) != n]

    print(coordinates)

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):   # 2 to 5 inclusive
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):  # 6 to 20 inclusive
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")