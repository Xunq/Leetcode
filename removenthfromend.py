# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:30:23 2016

@author: QiuXun

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.val = []
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # dummy points to the start of the linked list
        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        previous = dummy
        count = 1
                            
        while True:
            next_addr = current.next             

            if count-n>1:
                previous = previous.next
            
            if next_addr!=None:
                # move to next element in the list
                current = current.next
                count+=1
            else:
                previous.next = previous.next.next
                return dummy.next
                
# Test case
#head = ListNode(1)
#tail = ListNode(2)
#head.next=tail
#tail.next=None
#S = Solution()
#x=S.removeNthFromEnd(head,2)     
            
            
            