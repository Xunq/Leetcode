# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:36:01 2016

@author: QiuXun

Implements Insertionsort
"""

def Insertionsort(unsortlist):
   
   L = len(unsortlist)
   
   if L>1:
       for i in range(1,L):
       
           j = i
       
           while(j>=1 and unsortlist[j-1]>unsortlist[j]):
               # swap 
               unsortlist[j], unsortlist[j-1] = unsortlist[j-1], unsortlist[j]
               j-=1
   
   return unsortlist
    
           