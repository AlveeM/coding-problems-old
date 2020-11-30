class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
                
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow


class Solution2:
    def detectCycle(self, head):
        cur = head
        seen = set()
        
        while cur:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next