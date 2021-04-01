from sweepstakes import SweepStakes
import user_interface
from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack_manager import StackManager
from Stack import Stack
from myQueue import Queue

class Marketing_Firm:
    def __init__(self):
        self.manager = None

    def create_sweepstakes(self):
        sweepstakes = SweepStakes()
        stack_or_queue = user_interface.ask_firm_type_of_data_structure()
        if stack_or_queue == True:
            queue = Queue()
            self.manage_with_queue(sweepstakes, queue)
            winner = sweepstakes.pick_winner()
            sweepstakes.print_contestant_info(winner)
            print(queue)

        else:
            stack = Stack()
            self.manage_with_stack(sweepstakes, stack)
        winner = sweepstakes.pick_winner()
        sweepstakes.print_contestant_info(winner)
        print(stack)


    def manage_with_queue(self, sweepstakes, queue):
        self.manager = QueueManager()

        add_contestants = True
        while add_contestants:
            if not add_contestants:
                self.manager.add_sweepstakes(sweepstakes, queue)
                break
            else:
                sweepstakes.register_contestant()
                add_contestants = user_interface.add_more_contestants()


    def manage_with_stack(self, sweepstakes, stack):
        self.manager = StackManager()
        add_contestants = True
        while add_contestants:
            if not add_contestants:
                self.manager.add_sweepstakes(sweepstakes, stack)
                break
            else:
                sweepstakes.register_contestant()
                add_contestants = user_interface.add_more_contestants()
