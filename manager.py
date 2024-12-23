from multiprocessing.managers import BaseManager
import multiprocessing as mp
from queue import Queue

class QueueManager (BaseManager): pass



class QueueClient:
    def __init__(self):
        QueueManager.register('task_queue')
        QueueManager.register('result_queue')
        self.m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
        self.m.connect()
        self.task_queue = self.m.task_queue()
        self.result_queue = self.m.result_queue()


if __name__ == "__main__":
    taskqueue = Queue()
    resqueue = Queue()
    QueueManager.register('task_queue', callable=lambda:taskqueue)
    QueueManager.register('result_queue', callable=lambda:resqueue)
    m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()