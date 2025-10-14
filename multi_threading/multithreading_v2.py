import random
import threading
import time
from queue import Queue
from threading import Event


class ThreadOne(threading.Thread):
  def __init__(self, queue: Queue, stop_event: threading.Event):
    super().__init__()
    self._next_to_send = False
    self._queue = queue
    self._stop_event = stop_event

  def run(self):
    while not self._stop_event.is_set():
      time.sleep(1)
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
          print("Thread 1 - next iteration with:", current_random)


class ThreadTwo(threading.Thread):
  def __init__(
      self,
      queue_from_one: Queue,
      queue_to_three: Queue,
      stop_event: Event
  ):
    super().__init__()
    self._queue_from_one = queue_from_one
    self._queue_to_three = queue_to_three
    self._stop_event = stop_event
    self._last_from_queue = None
    self._sum = None

  def run(self):
    while not self._stop_event.is_set():
      time.sleep(1333 / 1000)
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


class ThreadThree(threading.Thread):
  def __init__(self, queue_from_two: Queue, stop_event: Event):
    super().__init__()
    self._queus_life_span = time.time()
    self._queue_from_two = queue_from_two
    self._stop_event = stop_event

  def run(self):
    while not self._stop_event.is_set():
      time.sleep(1)
      self._queus_life_span = time.time()
      if self._queue_from_two.qsize() == 1:
        self._queus_life_span = time.time()
      elif self._queue_from_two.qsize() >= 5:
        print("Thread 3: buffer has size 5")
        print("Thread 3 - elements:", list(self._queue_from_two.queue))
        self._queue_from_two.queue.clear()
      temp_buffer = list(self._queue_from_two.queue)
      sum_to_send = sum(temp_buffer)
      if sum_to_send > 117:
        print("Thread 3: sum of elements reached 117")
        print("Thread 3 - elements:", list(self._queue_from_two.queue))
        self._queue_from_two.queue.clear()
      if (time.time() - self._queus_life_span) > 30:
        print("Thread 3: first element arrived more than 30 second ago")
        print("Thread 3 - elements:", list(self._queue_from_two.queue))
        self._queue_from_two.queue.clear()


def main():
  print("Starting data exchange..")
  stop_event = Event()
  queue_one_and_two = Queue()
  queue_two_and_three = Queue()
  one_thread = ThreadOne(queue_one_and_two, stop_event)
  two_thread = ThreadTwo(queue_one_and_two, queue_two_and_three, stop_event)
  three_thread = ThreadThree(queue_two_and_three, stop_event)

  one_thread.start()
  two_thread.start()
  three_thread.start()

  one_thread.join()
  two_thread.join()
  three_thread.join()


main()
