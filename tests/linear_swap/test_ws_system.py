import sys
import unittest
import time

sys.path.append('../../src')
from huobi.utils.logger import logger
from huobi.linear_swap.ws.system import System


class TestWsSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = System()

    def test_sub_status(self):
        self.api.sub({"op": "sub", "topic": "public.linear-swap.heartbeat"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
