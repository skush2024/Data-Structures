"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
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

def bruteForce(head, n):
    count = 0

    current = head
    
    while current is not None :
        count += 1
        current = current.next

    pos = 0
    current = head

    if n == count :
        head = head.next
    
    else:
        while(pos < count - n - 1):
            current = current.next
            pos += 1
        
        current.next = current.next.next


def removeNthFromEnd(head, n):
    slow = head
    fast = head
    
    for i in range(n):
        fast = fast.next

    print(f"Slow at {slow.val}")
    print(f"Fast at {fast.val}")

    print(" ========== ")
    
    while fast.next is not None :
        slow = slow.next
        fast = fast.next
    
    print(f"Slow at {slow.val}")
    print(f"Fast at {fast.val}")
    print(" ========== ")

    
    
    slow.next = slow.next.next




if __name__ == "__main__":
    arr = [1,2,3,4,5]
    l1 = Solution(arr)
    l1.traverse()
    print(" ========== ")
    removeNthFromEnd(l1.head,5)
    l1.traverse()
