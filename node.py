class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next