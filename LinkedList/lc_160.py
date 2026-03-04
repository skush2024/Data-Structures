"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
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

    def merge_intersection(self, next_head):
        current = self.head
        while current.next is not None :
            current = current.next
        
        current.next = next_head


def bruteForce(headA, headB):
    current_a = headA
    current_b = headB

    while current_a is not None :
        current_a.visited = True
        current_a = current_a.next

    while current_b is not None :
        if 'visited' in vars(current_b):
            return current_b.val
        
        else :
            current_b.visited = True
            current_b = current_b.next
    
    return 



def bruteForce2(headA, headB):
    len_a = 0
    len_b = 0

    current_a = headA
    current_b = headB


    while(current_a is not None):
        len_a += 1
        current_a = current_a.next

    while(current_b is not None):
        len_b += 1
        current_b = current_b.next

    steps = abs(len_a - len_b)
    cnt = 0
    current_b = headB
    current_a = headA
    if len_a > len_b :
        while(cnt < steps) :
            current_a = current_a.next
            cnt += 1

    elif len_b > len_a:
        while(cnt < steps) :
            current_b = current_b.next
            cnt += 1
    
    while(current_a is not None and current_b is not None):
        if current_b == current_a :
            return current_b
        
        current_b = current_b.next
        current_a = current_a.next
    
    return


def getIntersectionNode(headA, headB):
    if (headA is None or headB is None):
        return


    temp1 = headA
    temp2 = headB

    while (temp1 != temp2) :
        temp1 = temp1.next
        temp2 = temp2.next

        if (temp1 == temp2):
            return temp1
        
        if (temp1 is None) :
            temp1 = headB
        
        if (temp2 is None) :
            temp2 = headA

    return temp1


if __name__ == "__main__" :
    arr1 = [1,9,1]
    arr2 = [3]
    intersection = [2,4]

    l1 = Solution(arr1)
    l2 = Solution(arr2)
    intersect = Solution(intersection)

    l1.merge_intersection(intersect.head)
    l2.merge_intersection(intersect.head)

    print(getIntersectionNode(l1.head, l2.head).val)


