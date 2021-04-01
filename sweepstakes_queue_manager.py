from node import Node


class QueueManager:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value_input):
        new_node = Node(value_input)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            return self

    def dequeue(self):
        if self.head is None:
            return "There are no nodes"
        value = self.head.value
        self.head - self.head.next
        return value

    def add_sweepstakes(self, sweepstake):
        self.StackManager.enqueue(sweepstake)

    def get_sweepstake(self, sweepstake):
        self.StackManager.enqueue(sweepstake)