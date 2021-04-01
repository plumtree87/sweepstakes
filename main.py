from sweepstakes import SweepStakes
from contestants import Contestant
from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack_manager import StackManager
from marketing_firm import Marketing_Firm
import user_interface

if __name__ == '__main__':
    stack_or_queue = user_interface.ask_firm_type_of_data_structure()
    sweepstakes = []
    while True:
        sweepstake = Marketing_Firm(stack_or_queue).add_new_sweepstake(stack_or_queue)
        if sweepstake[1] == True:
            sweepstake[0].queue
        if sweepstake[1] == False:
            sweepstake[0].stack


