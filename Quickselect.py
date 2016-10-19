# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:40:00 2016

@author: QiuXun

Quickselect: find the k-th smallest element in a list
"""

from Insertionsort import Insertionsort
from Quicksort import median3

def Quickselect(alist,k):
    
    L = len(alist)
    
    # assume k <= L
    if L == 1:
        return alist[0]
    elif L<4:
        alist = Insertionsort(alist)
        return alist[k-1]
    else:
        pivot, alist = median3(alist)
        
        left = 0
        right = L-2            
        swapdone = False
                
        while(not swapdone):
            left += 1
            right -= 1
                    
            while(alist[left]<pivot):
                left+=1
                        
            while(alist[right]>pivot):
                right-=1
                    
            if left < right:
                alist[left], alist[right] = alist[right], alist[left]
            else:
                swapdone = True

        alist[left], alist[L-2] = alist[L-2], alist[left]
                      
        if k < left+1:
            return Quickselect(alist[0:left],k)
        elif k == left+1:
            return pivot
        else:
            return Quickselect(alist[left+1:L],k-left-1)
           

#Quickselect([1,3,2,5,4],3)       
     
    