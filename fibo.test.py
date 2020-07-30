import unittest
import sys
from unittest.mock import Mock
# randMock = Mock()
# randMock.rand.return_value = 99
# sys.modules['rand'] = randMock;
import fibo


class TestFibo(unittest.TestCase):

    def test_fibo1(self):
        self.assertEqual(fibo.fib2(1), [0])

    def test_fibo2(self):
        self.assertEqual(fibo.fib2(2), [0, 1, 1])

    def test_fibo3(self):
        self.assertEqual(fibo.fib2(3), [0, 1, 1, 2])


if __name__ == '__main__':
    unittest.main()
