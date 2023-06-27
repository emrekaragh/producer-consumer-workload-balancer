import threading
import time

class TimedThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__time_elapsed = None

    def run(self):
        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

        """
        start_time = time.time()
        try:
            if self._target is not None:
                outputs = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        end_time = time.time()
        self.__time_elapsed = end_time - start_time
        return outputs

    def get_time_elapsed(self) -> float:    
        return self.__time_elapsed

if __name__ == '__main__':
    def my_target_function():
        time.sleep(2)  # Simulating some time-consuming operation
        return "Hello, world!"

    timed_thread = TimedThread(target=my_target_function)
    timed_thread.start()
    timed_thread.join()

    elapsed_time = timed_thread.get_time_elapsed()
    print(f"Time elapsed: {elapsed_time} seconds")
