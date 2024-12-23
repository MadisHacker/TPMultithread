import time
import json
import numpy as np


class Task:
    def __init__(self, identifier=0, size=1000):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start
    
    def to_json(self) -> str:
        val = json.dumps({"a":self.a.tolist(),"b" : self.b.tolist(),"size":self.size,"identifier":self.identifier})
        return val
    
    @staticmethod
    def from_json(text: str) -> "Task":
        res = Task()
        jsval = json.loads(text)
        res.a = np.array(jsval["a"])
        res.b = np.array(jsval["b"])
        res.size = jsval["size"]
        res.identifier = jsval["identifier"]
        return res


    def __eq__(self:"Task", other: "Task") -> bool:
        return ((self.a == other.a).all() and (self.b == other.b).all() and (self.size == other.size) and (self.identifier == other.identifier)) 


