# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 18:57:36 2017

@author: Claudio
"""

def quicksort(array):
    less = []; greater = []
    if len(array) <=1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)
    
print (quicksort([9,8,4,5,32,64,2,1,0,10,19,27]))
