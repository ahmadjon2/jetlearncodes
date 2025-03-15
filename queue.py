class Queeuuee:
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    def enqueue(self,item):
        if self.available == 0:
            print("queue is full")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1)%self.size
            self.available -= 1

    def dequeue(self):
        pass