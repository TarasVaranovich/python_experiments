import random
import threading
from threading import local


# TODO: for exchanging data between threads, use queue module
# https://docs.python.org/3/library/queue.html#module-queue

class ThreadOneLocal(local):
    next_to_send: bool = False

    def __init__(self):
        super().__init__()

    def update(self):
        current_random = random.randint(1, 6)
        if current_random == 3 and not self.next_to_send:
            print("Thread 1: tigger next value to sent")
            self.next_to_send = True
        else:
            if self.next_to_send:
                print(f"Thread 1 - sending value: {current_random}")
                self.next_to_send = False
            else:
                print("Thread 1 - next iteration")


def execute_thread_local(local: ThreadOneLocal):
    local.update()


def main():
    print("Starting data exchange..")
    localOne: ThreadOneLocal = ThreadOneLocal()
    thread = threading.Thread(target=execute_thread_local(localOne))
    thread.start()
    thread.join()


main()
