class Stack():
    def __init__(self,n):
        self.stack = []
        self.n = n       #maximn items added to stack
    def push(self,k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("the stack is full")
    def pop(self):
        if len(self.stack) < 1:
            print("stack is empty")
        else:
            self.stack.pop(-1)

    def display(self):
        print(self.stack)

    def size_stack(self):
        print(len(self.stack))

    def top(self):
        if len(self.stack) < 1:
            print("stack is empty")
        else:
            return self.stack[-1]
obj = Stack(6)
obj.display()
obj.push(7)
obj.display()
obj.push(5)
obj.push(9)
obj.push(8)
obj.display()
obj.push(5)
obj.push(9)
obj.push(8)
obj.display()
print(obj.top())
obj.pop()
obj.display()
obj.size_stack()
obj.display()