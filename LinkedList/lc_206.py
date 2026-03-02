"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def __init__(self, arr:list):
        prev_node = None
        for i in range(len(arr)):
            if i == 0 :
                self.head = ListNode(arr[i])
                prev_node = self.head
                continue

            new_node = ListNode(arr[i])
            prev_node.next = new_node
            prev_node = new_node

    def traverse(self) :
        current = self.head

        while current is not None: 
            print(current.val)
            current = current.next

    
    def reverseList(self):
        
        to_point = None 
        current = self.head

        while(current is not None):
            n_elem = current.next
            current.next = to_point
            to_point = current
            current = n_elem
        
        return to_point


    def recursivelyReverse(self, head):
        if head is None or head.next is None :
            return head
        
        new_head = self.recursivelyReverse(head.next)
    
        # Fix current connection
        head.next.next = head
        head.next = None
        
        return new_head



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    solver = Solution(arr)
    solver.head = solver.recursivelyReverse(solver.head)
    solver.traverse()
