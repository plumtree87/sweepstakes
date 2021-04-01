

class StackManager:
    def __init__(self):
        pass

    def add_sweepstakes(self, sweepstake, stack):
        stack.push(sweepstake)

    def get_sweepstake(self, sweepstake, stack):
        return stack.pop(sweepstake)
