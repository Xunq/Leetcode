# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:30:28 2016

@author: QiuXun

https://leetcode.com/problems/zigzag-conversion/
"""

class Solution(object):
    def __init__(self):
        self.vals = []          
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
           
        if numRows == 1:
            return s
        else:           
            L = len(s)
        
            stringlist = []
            for i in range(numRows):
                stringlist.append('')
            
            rownr = 0
            Zag = False
            for i in range(L):
                stringlist[rownr] = stringlist[rownr]+s[i]              
    
                if Zag==False:
                    if rownr == numRows-1:
                        rownr-=1
                        Zag = True
                    else:
                        rownr+=1
                else:
                    if rownr == 0:
                        rownr+=1
                        Zag = False
                    else:
                        rownr-=1        
                
            return ''.join(x for x in stringlist)
     
# Test case           
S=Solution()
S.convert("ABC", 1)