# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:17:41 2016

@author: QiuXun

Mergesort
"""

def Mergesort(unsortlist):
    '''
    In this code, Mergesort is performed
    '''
    L = len(unsortlist)
    
    left = 0
    right = L
    
    if(right-left>1):
        # if more than one element, sort each half and merge
        center = int((left+right)/2)
        sortlist_left = Mergesort(unsortlist[left:center])
        sortlist_right = Mergesort(unsortlist[center:right])
        sortlist = Merge(sortlist_left, sortlist_right)
        return sortlist
    else:
        # if only one element, return directly
        return unsortlist[:]
        
def Merge(sortlist_left, sortlist_right):
    '''
    Merge two sorted list
    '''
    
    L1 = len(sortlist_left)
    L2 = len(sortlist_right)
    
    sortlist_tmp = []
    
    L1_pointer = 0
    L2_pointer = 0
    
    while(L1_pointer < L1 and L2_pointer < L2):
        left_ele = sortlist_left[L1_pointer]
        right_ele = sortlist_right[L2_pointer]
        if left_ele < right_ele:
            sortlist_tmp.append(left_ele)
            L1_pointer = L1_pointer+1
        else:
            sortlist_tmp.append(right_ele)
            L2_pointer = L2_pointer+1

    if(L1_pointer < L1):
        sortlist_tmp.extend(sortlist_left[L1_pointer:L1])
        
    if(L2_pointer < L2):
        sortlist_tmp.extend(sortlist_right[L2_pointer:L2])
        
    return sortlist_tmp
    
    