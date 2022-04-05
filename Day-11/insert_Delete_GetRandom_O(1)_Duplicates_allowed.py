class RandomizedCollection:

    def __init__(self):
        self.list=dict()

    def insert(self, val: int) -> bool:
        if val not in self.list:
            self.list[val]=self.list.get(val,0)+1
            return True
        self.list[val]+=1
        return False

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.list[val]-=1
            if self.list[val]==0:
                del self.list[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choices(list(self.list.keys()))[0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()