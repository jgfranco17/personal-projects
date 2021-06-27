# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 18:16:23 2017

@author: Chino

Program designed to check if the input number is prime or not
"""

print("Prime number checker.")
num = int(input("Enter a number to check: "))

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(str(num) + " is not a prime number")
           print(str(num) + " is " + str(i) + " times " + str(num/i))
           break
   else:
       print(str(num) + " is a prime number")
else:
   print(str(num) + " is not a prime number")