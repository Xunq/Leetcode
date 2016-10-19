# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:29:40 2016

@author: QiuXun

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution(object):
    def __init__(self):
        self.val = []
   
   
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = len(nums)

        if L <=1:
            return L
        else:
            first = 0
            last = 1
        
            count = 1
            
            num_first = nums[first]                
            
            while count<L:                
                num_last = nums[last]
                
                if num_last == num_first:
                    del nums[last]
                else:
                    first = last
                    last = first+1
                  
                    if last > L:
                        return len(nums)
                    else:
                          num_first = nums[first]                
                
                count+=1
                       
            
            return len(nums)

# Test case
S = Solution()
S.removeDuplicates([1,1,2])
S.removeDuplicates([1,2,2])