import threading
from queue import Queue

from timed_thread import TimedThread

class Consumer(TimedThread):
    def __init__(self, queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__queue = queue
    
    def run(self):
        data = self.__queue.get()
        self._args += (data, )
        super().run()

if __name__ == '__main__':

    from producer import Producer

    def f_producer(n):
        return n
    
    def f_consumer(data):
        print('Consumer gets:', data)

    shared_queue = Queue()
    
    # Create a consumer thread
    consumer = Consumer(queue=shared_queue, target=f_consumer)
    consumer.start()
    
    producer = Producer(queue=shared_queue, target=f_producer, args=(1, ))
    producer.start()
    
    producer.join()
    consumer.join()

    print(f"Producer time elapsed: {producer.get_time_elapsed()} seconds")
    print(f"Consumer time elapsed: {consumer.get_time_elapsed()} seconds")

    # Print the data produced by the producer
    while not shared_queue.empty():
        data = shared_queue.get()
        print(f"queue item: {data}")
