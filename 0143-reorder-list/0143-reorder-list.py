class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # STEP 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # break list
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # STEP 3: Merge two halves
        first, second = head, prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2