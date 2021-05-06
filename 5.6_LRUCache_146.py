class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        

    def get(self, key: int) -> int:
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key) #  相当于换新；python 的 dictionary自动把它放到后面
            self.dic[key] = value
        elif len(self.dic) < self.capacity:
            self.dic[key] = value
        else:
            self.dic.pop(next(iter(self.dic)))
            self.dic[key] = value
        return
        