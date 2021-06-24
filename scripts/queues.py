import queue

class EffectQueue():
    _queue = None

    def __new__(cls) -> queue.Queue:
        if cls._queue is None:
            cls._queue = queue.Queue()
        return cls._queue

class SubEffectQueue():
    _queue = None

    def __new__(cls) -> queue.Queue:
        if cls._queue is None:
            cls._queue = queue.Queue()
        return cls._queue
