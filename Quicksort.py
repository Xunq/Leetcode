# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:06:53 2016

@author: QiuXun

Quicksort
"""
from Insertionsort import Insertionsort

def Quicksort(unsortlist):
    
    L = len(unsortlist)
    
    if (L>=3):
        pivot, unsortlist = median3(unsortlist)
        
        left = 0
        right = L-2
        
        swapdone = False
        while(not swapdone):
            # move left pointer right until element>=pivot        
            left+=1  #! important to move the pointer before doing comparison            
            while(unsortlist[left]<pivot):
                left+=1

            # move right pointer left until element<=pivot
            right-=1            
            while(unsortlist[right]>pivot):
                right-=1
        
            if(left<right):
                unsortlist[left], unsortlist[right] = \
                unsortlist[right], unsortlist[left]
            else:
                swapdone = True
        
        unsortlist[left], unsortlist[L-2] = unsortlist[L-2], unsortlist[left]
 
        unsortlist[0:left] = Quicksort(unsortlist[0:left])
        unsortlist[left+1:L] = Quicksort(unsortlist[left+1:L])
        
        return unsortlist
        
    else:
        return Insertionsort(unsortlist)
        

def median3(unsortlist):
    L = len(unsortlist)
    right = L-1
    center = int(right/2)
    
    if(unsortlist[0]>unsortlist[center]):
        unsortlist[0], unsortlist[center] = unsortlist[center], unsortlist[0]
    
    if(unsortlist[0]>unsortlist[right]):
        unsortlist[0], unsortlist[right] = unsortlist[right], unsortlist[0]
    
    if(unsortlist[center]>unsortlist[right]):
        unsortlist[center], unsortlist[right] = \
        unsortlist[right], unsortlist[center]
        
    unsortlist[center], unsortlist[right-1] = \
    unsortlist[right-1], unsortlist[center]
    
    return unsortlist[right-1], unsortlist
    
sortlist = Quicksort([2,1,0,5,3])
