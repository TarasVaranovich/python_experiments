import random
import threading
import time
from threading import Event
from threading import local


# Stack size, timeout, thread local data
# Thread object
# Daemon -> Event
# TODO: for exchanging data between threads, use queue module
# https://docs.python.org/3/library/queue.html#module-queue

class OneThreadLocal(local):
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
                print(f"Thread 1 - next iteration with: {current_random}")


def one_execute_thread_local(local: OneThreadLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1)
        local.update()


class TwoThreadLocal(local):

    def __init__(self):
        super().__init__()

    def update(self):
        current_random = random.choice([10, 20, 30])
        print("Thread 2: generated value:", current_random)


def two_execute_thread_local(local: TwoThreadLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1333 / 1000)
        local.update()


def main():
    print("Starting data exchange..")
    one_stop_event = Event()
    one_thread = threading.Thread(target=one_execute_thread_local, args=(OneThreadLocal(), one_stop_event))
    # TODO: How to stop the thread gracefully?
    two_stop_event = Event()
    two_thread = threading.Thread(target=two_execute_thread_local, args=(TwoThreadLocal(), two_stop_event))

    one_thread.start()
    two_thread.start()

    one_thread.join()
    two_thread.join()

    one_stop_event.set()
    two_stop_event.set()

main()