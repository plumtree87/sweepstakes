class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next