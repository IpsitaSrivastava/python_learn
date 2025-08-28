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