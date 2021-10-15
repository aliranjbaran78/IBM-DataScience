# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:11:29 2021

@author: Ali
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
        if largest == None :
            largest=num
        elif num > largest:
            largest= num
        if smallest == None :
            smallest=num
        elif num < smallest:
            smallest= num
    except:
        num= num
        
print('Invalid input')
print('maximum is ', largest)
print('minimum is ', smallest)