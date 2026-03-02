"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
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

    
    def middleNode(self):
        slow = self.head
        fast = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    solver = Solution(arr)
    middle = solver.middleNode()
    print(middle.val)