'''Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4'''

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key  # Fix: Store the key correctly
        self.val = val  # Store the value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary for O(1) access: {key: ListNode}

        # Dummy head and tail to simplify operations
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        """Adds a node right after the head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node):
        """Moves an existing node to the front (most recently used)."""
        self._remove_node(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        """Returns value if key exists; otherwise, return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  # Move accessed node to front
            return node.val
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        """Inserts/updates a key-value pair and evicts LRU if necessary."""
        if key in self.cache:
            node = self.cache[key]
            node.val = value  # Update value
            self._move_to_front(node)  # Move to front
        else:
            if len(self.cache) >= self.capacity:
                # Remove the Least Recently Used (LRU) node
                lru_node = self.tail.prev  # This is the LRU node
                self._remove_node(lru_node)
                del self.cache[lru_node.key]  # Fix: Correctly delete using attribute `key`

            # Add the new node
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
