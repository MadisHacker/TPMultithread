from multiprocessing.managers import BaseManager
import multiprocessing as mp
from queue import Queue
taskqueue = Queue()
resqueue = Queue()
class QueueManager (BaseManager): pass
QueueManager.register('task_queue', callable=lambda:taskqueue)
QueueManager.register('result_queue', callable=lambda:resqueue)
m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()