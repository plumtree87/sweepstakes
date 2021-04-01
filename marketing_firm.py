from sweepstakes import SweepStakes
import user_interface
from sweepstakes_queue_manager import QueueManager
from sweepstakes_stack_manager import StackManager
from Stack import Stack
from myQueue import Queue

class Marketing_Firm:
    def __init__(self, stack_or_queue):
        self.manager = stack_or_queue

    def create_sweepstakes(self):
        sweepstakes = SweepStakes()
        if self.manager == True:
            queue = Queue()
            self.manage_with_queue(sweepstakes, queue)
            winner = sweepstakes.pick_winner()
            sweepstakes.print_contestant_info(winner)
            return queue

        if self.manager == False:
            stack = Stack()
            self.manage_with_stack(sweepstakes, stack)
        winner = sweepstakes.pick_winner()
        sweepstakes.print_contestant_info(winner)

        return stack


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
        queue.enqueue(sweepstakes)


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
                self.manager.add_sweepstakes(add_contestants)
        stack.push(sweepstakes)

    def add_new_sweepstake(self, stack_or_queue):
        keep_creating_new_sweepstakes = "Nothing yet"
        while keep_creating_new_sweepstakes != False:
            if keep_creating_new_sweepstakes == True:
                firm = Marketing_Firm(stack_or_queue)
                managed_sweepstakes = firm.create_sweepstakes()
                return managed_sweepstakes
            else:
                keep_creating_new_sweepstakes = user_interface.create_new_sweepstake()

