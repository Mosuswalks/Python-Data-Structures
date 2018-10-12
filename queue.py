

class Queue:

    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0

    def enqueue(self, obj):
        self.q.insert(0, obj)

    def dequeue(self):
        return self.q.pop()

    def size(self):
        return len(self.q)

if __name__ == '__main__':
    qq = Queue()
    print(qq.isEmpty())
    qq.enqueue('Data Object')
    print(qq.size())
    qq.dequeue()
    print(qq.size())
    

    
