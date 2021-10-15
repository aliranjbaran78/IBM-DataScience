# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 19:15:24 2021

@author: Ali
"""

fruit='banana'
index= 0
while index <len(fruit):
    letter = fruit[index]
    print(index,'letter')
    index=index +1

#find in strings
pos = fruit.find('an')
if pos ==-1:
    print('Not in Text')
else:
    print(pos)
    
filex= open('ali.txt','r')
print(filex)
#nxt line
print('hello\nworld')
cnt=0
for Line in filex:
    cnt+=1
print('line count: ',cnt)

cct=0
for Line in filex:
    if line.startswith('be name khoda'):
        cct +=1
print('line cct: ',cct)
    