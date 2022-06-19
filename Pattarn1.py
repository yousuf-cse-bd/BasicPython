# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:09:57 2020

@author: yousuf
"""

n = input('Enter a Positive Value Here: ');
n = int(n);

for i in range(1,n+2,1):
    for j in range(1,i,1):
        print(j)
    print('\n');
print('End Loop');

