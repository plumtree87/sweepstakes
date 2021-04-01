
class Stack:
    def __init__(self):
        stack = []

    def push(self, value_input):
        self.stack.append(value_input)

    def pop(self):
        self.stack.remove(self.stack[len(self.stack) - 1])