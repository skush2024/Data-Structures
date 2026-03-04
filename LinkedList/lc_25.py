"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
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



def reverse(head): 
    prev_elem = None
    current = head
    
    while(current is not None):
        next_elem = current.next
        current.next = prev_elem
        prev_elem = current
        current = next_elem

    return prev_elem, head


def reverseKGroup(Node, k):
    if k == 1 :
        return Node

    current = Node.head
    
    nodes = []

    n = 0
    
    last_head = None
    
    while(current is not None):
        if n == 0 :
            last_head = current
            current = current.next
            n += 1
        
        elif n == k - 1 :
            nodes.append(last_head)
            next_elem = current.next
            current.next = None
            current = next_elem
            last_head = None
            n = 0

        else :
            n += 1
            current = current.next


    new_head = None
    prev_tail = None

    for node in nodes :
        group_head, tail = reverse(node)
        if new_head is None :
            new_head = group_head
            prev_tail = tail
        
        else :
            prev_tail.next = group_head
            prev_tail = tail

    prev_tail.next = last_head
    return new_head        

if __name__ == "__main__" :
    arr = [1,2,3,4,5]
    l1 = Solution(arr)
    nh = reverseKGroup(l1,1)
    temp = nh 
    
    while(temp is not None):
        print(temp.val)
        temp = temp.next


