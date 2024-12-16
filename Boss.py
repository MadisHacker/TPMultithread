from multiprocessing.managers import BaseManager
from task import Task
class Boss(BaseManager): pass
Boss.register('task_queue')
Boss.register('result_queue')
m = Boss(address=('localhost', 50000), authkey=b'abracadabra')
m.connect()
task_queue = m.task_queue()
result_queue = m.result_queue()

for i in range(10):
    task_queue.put(Task(i))
for i in range(10):
    res= result_queue.get()
    