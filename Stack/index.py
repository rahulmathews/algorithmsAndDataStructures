class Stack:
    def __init__(self, length):
        self.data = []
        self.length = length

    def push(self, elem):
        if len(self.data) is self.length:
            print('Overflow')
            return

        self.data.append(elem)

    def pop(self):
        if not self.data:
            print('Underflow')
            return

        self.data.pop()

    def display(self):
        print(self.data)
        return

#Intialise
stack = Stack(5)

stack.push(4)
stack.push(2)
stack.push(6)
stack.push(7)
stack.push(1)
stack.push(0)
stack.pop()
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()
