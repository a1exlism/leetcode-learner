"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity)
-- 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key
-- 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 
-- 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
-- 当缓存容量达到上限时，它应该在写入新数据之前`删除最久未使用的数据值`，从而为新的数据值留出空间。
"""


from collections import OrderedDict


class DualLinkedList():
    def __init__(self, key: int = None, val: int = None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    HashTable + Double Linked List
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.size = 0
        self._head = DualLinkedList()
        self._tail = DualLinkedList()
        # IMPORTANT
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.node_remove(node)
            self.node_add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        # 1. remove LRU key;
        if key not in self.cache and len(self.cache) == self.cap:
            removed_key = self.node_remove_head()
            self.cache.pop(removed_key)
        # 2. insert | update
        if key in self.cache:
            self.node_remove(self.cache[key])
        node = DualLinkedList(key, val)
        self.cache[key] = node
        # 3. update queue-linklist
        self.node_add_to_tail(node)

    def node_add_to_tail(self, node: DualLinkedList) -> None:
        # ->
        prev = self._tail.prev
        prev.next = node
        node.next = self._tail
        # <-
        self._tail.prev = node
        node.prev = prev

    def node_remove_head(self) -> int:
        real_h = self._head.next
        _next = real_h.next
        self._head.next = _next
        _next.prev = self._head
        return real_h.key

    def node_remove(self, node: DualLinkedList) -> None:
        _prev, _next = node.prev, node.next
        _prev.next = _next
        _next.prev = _prev


class LRUCache2:
    """
    collections.OrderedDict()
    od.move_to_end(_key)
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)


class LRUCache3:
    """ with Queue """

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lru = []
        pass

    def upd(self, _key: int) -> None:
        self.lru.remove(_key)
        self.lru.append(_key)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.upd(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.upd(key)
            return
        if len(self.cache) == self.cap:
            key_to_remove = self.lru.pop(0)
            self.cache.pop(key_to_remove)
        self.cache[key] = value
        self.lru.append(key)


if __name__ == '__main__':
    pass
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
