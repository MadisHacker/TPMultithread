from multiprocessing.managers import BaseManager
class Minion(BaseManager): pass
Minion.register('task_queue')
Minion.register('result_queue')
m = Minion(address=('localhost', 50000), authkey=b'abracadabra')
m.connect()

task_queue = m.task_queue()
result_queue = m.result_queue()
i=0
while (task_queue.qsize()>0):
    t = task_queue.get()
    i = i+1
    t.work()
    print("tache ", t.identifier," effectuée avec un temps de ", t.time)
    result_queue.put(t)