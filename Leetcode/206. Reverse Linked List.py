# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):

        sol = []
        sol.append(head)
        return sol

input = [1,2,3,4,5]
print(Solution().reverseList(ListNode(1)))