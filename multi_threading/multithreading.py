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
                print(f"Thread 1 - next iteration with: {current_random}")


def execute_thread_local(local: ThreadOneLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1)
        local.update()


def main():
    print("Starting data exchange..")
    stop_event = Event()
    thread = threading.Thread(target=execute_thread_local(ThreadOneLocal(), stop_event))
    thread.start()
    thread.join()
    # How to stop the thread gracefully?
    stop_event.set()


main()
