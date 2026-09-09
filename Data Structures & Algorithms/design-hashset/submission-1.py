class MyHashSet:

    def __init__(self):
        self.hmap = {}

    def add(self, key: int) -> None:
        self.hmap[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hmap[key]

    def contains(self, key: int) -> bool:
        return key in self.hmap


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)