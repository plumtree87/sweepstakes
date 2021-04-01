from sweepstakes import SweepStakes
from contestants import Contestant
from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack_manager import StackManager
from marketing_firm import Marketing_Firm

if __name__ == '__main__':

    firm = Marketing_Firm()
    firm.create_sweepstakes()
