import random
import threading
import time
from asyncio import Queue
from threading import Event
from threading import local


# Stack size, timeout, thread local data
# Thread object
# Daemon -> Event
# TODO: for exchanging data between threads, use queue module
# https://docs.python.org/3/library/queue.html#module-queue

class OneThreadLocal(local):

    def __init__(self, queue: Queue):
        self._next_to_send = False
        self._queue = queue
        super().__init__()

    def update(self):
        current_random = random.randint(1, 6)
        if current_random == 3 and not self._next_to_send:
            print("Thread 1: tigger next value to sent")
            self._next_to_send = True
        else:
            if self._next_to_send:
                print("Thread 1 - sending value:", current_random)
                self._queue.put_nowait(current_random)
                self._next_to_send = False
            else:
                print(f"Thread 1 - next iteration with:", current_random)


def one_execute_thread_local(local: OneThreadLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1)
        local.update()


class TwoThreadLocal(local):

    def __init__(self, queue_from_one: Queue, queue_to_three: Queue):
        self._queue_from_one = queue_from_one
        self._queue_to_three = queue_to_three
        self._last_from_queue = None
        self._sum = None
        super().__init__()

    def update(self):
        current_random = random.choice([10, 20, 30])
        print("Thread 2 actual generated value:", current_random)

        if self._last_from_queue is None:
            print("Thread 2 - queue is empty, waiting for value")
        else:
            self._sum = current_random + self._last_from_queue
            print("Thread 2 actual sum:", self._sum)

        if not self._queue_from_one.empty():
            self._last_from_queue = self._queue_from_one.get_nowait()
            sum_to_send = current_random + self._last_from_queue
            self._queue_to_three.put_nowait(sum_to_send)
            print("Thread 2 sent sum to Thread 3 :", self._sum)


def two_execute_thread_local(local: TwoThreadLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1333 / 1000)
        local.update()


class ThreeThreadLocal(local):
    buffer = list()

    def __init__(self, queue_from_two: Queue):
        self._queue_from_two = queue_from_two
        super().__init__()

    def update(self):
        # Queue to three can be as buffer
        print("Thread 3 buffer:", self.buffer)


def three_execute_thread_local(local: ThreeThreadLocal, stop_event: Event):
    while not stop_event.is_set():
        time.sleep(1)
        local.update()


def main():
    print("Starting data exchange..")
    stop_event = Event()
    queue_one_and_two = Queue()
    queue_two_and_three = Queue()
    one_thread = (
        threading.Thread(target=one_execute_thread_local, args=(OneThreadLocal(queue_one_and_two), stop_event)))
    two_thread = (
        threading.Thread(
            target=two_execute_thread_local,
            args=(TwoThreadLocal(queue_one_and_two, queue_two_and_three), stop_event)
        )
    )
    three_thread = (
        threading.Thread(target=two_execute_thread_local, args=(ThreeThreadLocal(queue_two_and_three), stop_event)))

    one_thread.start()
    two_thread.start()
    # three_thread.start()

    one_thread.join()
    two_thread.join()
    # three_thread.join()

    stop_event.set()
    # TODO: How to stop the thread gracefully?
    # TODO: add with clause to threads


main()
