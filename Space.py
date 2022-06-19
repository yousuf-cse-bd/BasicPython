# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:39:53 2020

@author: yousuf
"""
def space(n):
    n = int(n);
    for i in range(0,n+1,1):
        print(' ');
space(2);   
firstName = 'Muhammad';
lastName = 'Yousuf';
print(firstName+space(2)+lastName);
