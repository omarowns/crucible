import queue

class EffectQueue():
    _queue = None

    def __new__(cls):
        if cls._queue is None:
            cls._queue = queue.Queue()
        return cls._queue

    @classmethod
    def get(cls):
        cls._queue.get()

    @classmethod
    def put(cls, effect):
        cls._queue.put(effect)
    
    @classmethod
    def join(cls):
        cls._queue.join()
    
    @classmethod
    def task_done(cls):
        cls._queue.task_done()