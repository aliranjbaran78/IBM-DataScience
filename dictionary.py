# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:11:30 2021

@author: Ali
"""

#dict
karndict = {'name':'ali',
            'shoghl':'bikar'}
w=input('yek kalame vared knid: ')
v={'a':0,
   'o':0,
   'e':0,
   'i':0,
   'u':0}
for k in w:
    if k in v:
        v[k]+=1
for k in v:   
    print(k,' was found',v[k], 'times')
#print both key\value
for k,j in sorted(v.items()):
    print(k,' was found', j, 'times')
#sort by alphab
for k in sorted(v):
    print(k,' was found',v[k], 'times')

#if not by set.default
difaloy={}
difaloy.setdefault(input('no aloy ra vared knid: '),0)

#dict in dict
scientists={'nikola':{'Full name':'Nikola Tesla',
                      'Born':'1856,croatia'},
            'Maryam':{'Full name':'Maryam Mirzakhani',
                      'Born':'1977,Tehran'}}
import pprint 
#pprint.pprint(name)
