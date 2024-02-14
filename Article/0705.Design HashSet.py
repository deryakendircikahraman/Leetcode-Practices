# 705. Design HashSet
# Easy
#
# Topics: Design

#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
# * void add(key) Inserts the value key into the HashSet.
# * bool contains(key) Returns whether the value key exists in the HashSet or not.
# * void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
#
# Example 1:
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
# Constraints:
# * 0 <= key <= 10^6
# * At most 10^4 calls will be made to add, remove, and contains.

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None  # Initialize next to None


class MyHashSet(object):
    def __init__(self):
        self.set = [ListNode(0) for i in range(10 ** 4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False  # Corrected 'false' to 'False'



 # Example usage:
if __name__ == "__main__":
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        print(myHashSet.contains(1))  # Output: True
        print(myHashSet.contains(3))  # Output: False
        myHashSet.add(2)
        print(myHashSet.contains(2))  # Output: True
        myHashSet.remove(2)
        print(myHashSet.contains(2))  # Output: False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

