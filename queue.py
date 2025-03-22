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
        if self.available == self.size:
            print("queue is empty")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1)%self.size
            self.available += 1

    def peek(self):
        print(self.queue[self.front])

    def printq(self):
        print(self.queue)

que = Queeuuee(5)
que.printq()
que.enqueue(2)
que.enqueue(9)
que.enqueue(7)
que.enqueue(3)
que.enqueue(5)
que.peek()
que.dequeue()
que.printq()
que.enqueue(6)
que.printq()
que.peek()