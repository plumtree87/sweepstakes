
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value_input):
        self.queue.append(value_input)

    def dequeue(self):
        self.queue[0].remove()
