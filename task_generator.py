import inspect

class TaskGenerator:
    def __init__(self, generator_func):
        if not inspect.isgeneratorfunction(generator_func):
            raise ValueError("The provided function is not a generator function.")
        self.generator_func = generator_func
        self.generator = None

    def start(self):
        self.generator = self.generator_func()

    def get_next_task(self):
        if self.generator is None:
            raise RuntimeError("The generator has not been started.")
        try:
            task = next(self.generator)
            return task
        except StopIteration:
            return None

if __name__ == '__main__':

    def task_generator():
        yield "Task 1"
        yield "Task 2"
        yield "Task 3"

    generator = TaskGenerator(task_generator)

    generator.start()

    while True:
        task = generator.get_next_task()
        if task is None:
            break
        print("Next Task:", task)

