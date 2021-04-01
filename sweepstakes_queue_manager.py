from node import Node
from myQueue import Queue

class QueueManager:
    def __init__(self):
        pass

    def add_sweepstakes(self, sweepstake):
        sweepstake.myQueue().enqueue(sweepstake)

    def get_sweepstake(self, sweepstake):
        sweepstake.myQueue().enqueue(sweepstake)