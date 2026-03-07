"""
Given the head of a linked list, rotate the list to the right by k places.
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



def rotateRight(head : ListNode, k : int):
    

    if head is None or head.next is None or k == 0:
        return head

    length = 0
    current = head
    while(current is not None):
        length += 1
        current = current.next

    k = k % length
    if k == 0:
        return head

    slow = head
    fast = head

    steps = 0
    while(steps < k):
        fast = fast.next
        steps += 1

    prev_elem = None
    
    while (fast is not None):
        prev_elem = slow
        slow = slow.next
        fast = fast.next

    new_head = slow
    prev_elem.next = None

    tail = new_head
    while(tail.next is not None):
        tail = tail.next
    
    tail.next = head

    return new_head

    
    







if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    l1 = Solution(arr)

    nh = rotateRight(l1.head, 10)

    current = nh
    while(current is not None): 
        print(f"{current.val}", end = " -> ")
        current = current.next

