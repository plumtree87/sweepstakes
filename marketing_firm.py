from sweepstakes import SweepStakes
import user_interface
from sweepstakes_stack_manager import StackManager


class Marketing_Firm:
    def __init__(self):
        self.manager = None

    def create_sweepstakes(self):
        sweepstakes = SweepStakes()
        self.manager = StackManager()
        self.manager.add_sweepstake(sweepstakes)


