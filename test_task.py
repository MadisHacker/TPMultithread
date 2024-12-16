import numpy as np
import unittest
from task import Task

class TestStringMethods(unittest.TestCase):
    def test_work(self):
        task = Task()
        task.work()
        np.testing.assert_allclose(np.dot(task.a, task.x), task.b, rtol=1e-5, atol=1e-8)

    def test_json(self):
        a = Task()
        txt = a.to_json()
        b = Task.from_json(txt)
        print(a==b)

if __name__ == "__main__":
    unittest.main()
