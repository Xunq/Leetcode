# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:45:24 2016

@author: QiuXun

https://leetcode.com/problems/longest-common-prefix/
"""

class Solution(object):
    def __init__(self):
        self.vals = []     

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = ''
        
        L = len(strs)       
    
        if L == 0:
            return ''
        
        index = 0
        newchar = ''
        
        strlen = []

        for i in range(L):
            tmp_len = len(strs[i])
            if tmp_len == 0:
                return ''
            else:
                strlen.append(len(strs[i]))        
        
        while True:
            if index >= strlen[0]:
                return longest_prefix
            else:
                longest_prefix = longest_prefix+strs[0][index]
                newchar = longest_prefix[-1]
                for i in range(1,L):    
                    if index >= strlen[i] or strs[i][index] != newchar:
                        return longest_prefix[0:-1]
            
            index+=1
                    
#S = Solution()
#tmp=['apple','apple1']
#S.longestCommonPrefix(tmp)
        
        