from node import Node


class StackManager:
    def __init__(self):
        self.top = None

    def push(self, value_input):
        new_node = Node(value_input)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        return self

    def pop(self):
        if self.top is None:
            return "This Stack is Empty"
        else:
            temp = self.top.value
            self.top = self.top.next
        return temp

    def add_sweepstakes(self, sweepstake):
        self.StackManager.push(sweepstake)

    def get_sweepstake(self, sweepstake):
        self.StackManager.pop(sweepstake)
