import threading
from queue import Queue

from timed_thread import TimedThread

class Producer(TimedThread):
    def __init__(self, queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__queue = queue

    def run(self):
        outputs = super().run()
        self.__queue.put(outputs)


if __name__ == '__main__':
    def f(n):
        return n

    shared_queue = Queue()
    producer = Producer(queue=shared_queue, target=f, args=(1, ))
    producer.start()
    producer.join()

    # Stop the producer thread

    print(f"Time elapsed: {producer.get_time_elapsed()} seconds")

    # Print the data produced by the producer
    while not shared_queue.empty():
        data = shared_queue.get()
        print(f"Produced data: {data}")
