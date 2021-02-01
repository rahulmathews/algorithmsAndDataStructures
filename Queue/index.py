class Queue:
    def __init__(self, length):
        self.data = []
        self.length = length

    def enqueue(self, elem):
        if len(self.data) is self.length:
            print('Overflow')
            return
        
        self.data.append(elem)

    def dequeue(self):
        if not self.data:
            print('UnderFlow')
            return

        self.data.pop(0)

    def display(self):
        print(self.data)
        return

#Intialise Queue
queue = Queue(4)
queue.enqueue(1)
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(9)
queue.enqueue(4)
queue.display()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()