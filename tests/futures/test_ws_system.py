import sys
import unittest
import time

sys.path.append('../../src')
from huobi.futures.ws.system import System
from huobi.utils.logger import logger


class TestWsSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = System()

    def test_sub_status(self):
        self.api.sub({"op": "sub", "topic": "public.futures.heartbeat"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
