# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:15:59 2016

@author: QiuXun

https://leetcode.com/problems/two-sum/
"""

class Solution(object):

    def __init__(self):
        self.vals = []       
        
    def twoSum(self, nums, target):
        # construct a dictionary from the list 'nums'
        # with value as keys and indices as value
        dict_num = dict()
        
        L = len(nums)        
        index = 0
        for i in nums:
            # if there are several indices with the same value
            # put all indices in a list
            dict_num[i] = dict_num.get(i,[])+[index]
            index+=1
        
        keys_dict = dict_num.keys()
        
        for i in range(L):
            var1 = nums[i]
            var2 = target - var1
            
            if var1==var2:
                # only return if they are in different positions
                if len(dict_num[var1])>1:
                    return dict_num[var1]
            else:
                if var2 in keys_dict:
                    j = dict_num[var2]
                    return [i]+j
                           
        
# Test case                
S = Solution()
S.twoSum([0,4,3,0],0)