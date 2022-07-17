import unittest

import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        result = main.helloworld("Test")
        self.assertEquals('hello world! Chris', result)


if __name__ == '__main__':
    unittest.main()
