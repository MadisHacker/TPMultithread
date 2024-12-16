import numpy as np
import unittest
from task import Task

class TestStringMethods(unittest.TestCase):
    def test_work(self):
        task = Task()
        task.work()
        np.testing.assert_allclose(np.dot(task.a, task.x), task.b, rtol=1e-5, atol=1e-8)

if __name__ == "__main__":
    unittest.main()
