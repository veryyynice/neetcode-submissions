class Node:
    def __init__(self,key,val):
        self.key,self.val = key, val
        self.next,self.prev = None, None
class LRUCache:
    #LRU is we override which over thing got created/visited last
    def __init__(self, capacity: int):
        self.cache = {} #maps key to Node in linked_list
        self.capacity = capacity
        self.start,self.end = Node(0,0),Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start    

    def remove(self,node):
        prev,nxt = node.prev,node.next

        prev.next = nxt
        nxt.prev =prev
    def insert(self,node):
        prev,nxt = self.end.prev, self.end
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev 
    def get(self, key: int) -> int:
        #view
        res = self.cache.get(key,-1)
        if res != -1:
            ans = res.val
            #move this Node to the end
            #remove node 
            #insert node
            self.remove(res)
            self.insert(res)
            return ans
        return (-1)

    def put(self, key: int, value: int) -> None:
        #if key in cache, update, otherwise add to the cache keeping capacity
        if key in self.cache:
            curr_node = self.cache[key] 
            curr_node.val = value
            #move this Node to the end 
            self.remove(curr_node)
            self.insert(curr_node)
            return
        
        #if cache full evict first 
        if len(self.cache) >= self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.insert(new_node)
