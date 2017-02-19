#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    print((((n//3)*3*(1+(n//3)))//2 + ((n//5)*5*(1+(n//5)))//2 - ((n//15)*15*(1+(n//15)))//2))
   
