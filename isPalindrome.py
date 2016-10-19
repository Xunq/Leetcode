# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:30:16 2016

@author: QiuXun

https://leetcode.com/problems/palindrome-number/
"""

class Solution(object):
    def __init__(self):
        self.vals = []     
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        strx = str(x)
        
        L = len(strx)
        
        if L <=1:
            return True
        else:
            if strx[0]==strx[-1]:
                strx  = strx[1:-1]
            
                S = Solution()            
            
                return S.isPalindrome(strx)
            else:
                return False
        
    def isPalindrome2(self,x):
        if x<0:
            return False
        else:
            return x==int(str(x)[::-1])
        