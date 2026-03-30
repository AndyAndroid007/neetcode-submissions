# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        newlist = ListNode()
        head = newlist

        i = list1
        j = list2

        while i and j:
            print(i.val,j.val)
            if i.val < j.val:
                newlist.next = i
                i = i.next
            else:
                newlist.next = j
                j = j.next
            newlist = newlist.next
        while i:
            newlist.next = i
            i = i.next
            newlist = newlist.next
        while j:
            newlist.next = j
            j = j.next
            newlist = newlist.next
        return head.next

            

        