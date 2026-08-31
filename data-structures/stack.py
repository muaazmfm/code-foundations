class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()

    def peak(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, i):
        self.stack.append(i)


if __name__ == "__main__":
    stack = Stack()
    for i in range(4):
        stack.push(i+1)

    for j in range(5):
        print(stack.peak())

    for k in range(5):
        print(stack.pop())
