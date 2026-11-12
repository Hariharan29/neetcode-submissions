class MyHashMap(object):
    class ListNode:
        def __init__(self,key=-1,val=-1,next=None):
            self.key=key
            self.val=val
            self.next=next

    def __init__(self):
        self.size = 1000
        self.hmap = [self.ListNode() for r in range(self.size)]
        
    def hash(self,key):
        return key%len(self.hmap)

    def put(self, key, value):
        cur = self.hmap[self.hash(key)]
        while cur.next:
            if cur.next.key==key:
                cur.next.val = value
                return
            cur=cur.next
        cur.next = self.ListNode(key,value)
            
    def get(self, key):
        cur = self.hmap[self.hash(key)].next
        while cur:
            if cur.key==key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        cur = self.hmap[self.hash(key)]
        while cur and cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
            cur = cur.next
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)