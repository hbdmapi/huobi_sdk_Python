import sys
import unittest
import time

sys.path.append('../../src')
sys.path.append('..')
from huobi.utils.logger import logger
from huobi.spot.ws.account import Account
from config import ACCESS_KEY, SECRET_KEY


class TestWsAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Account(ACCESS_KEY, SECRET_KEY)

    def test_sub_orders(self):
        self.api.sub({"action": "sub", "ch": "orders#trxusdt"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"action": "unsub", "ch": "orders#trxusdt"})
        time.sleep(10)

    def test_sub_accounts(self):
        self.api.sub({"action": "sub", "ch": "accounts.update#1"},
                     lambda x: logger.info(x))
        time.sleep(30)
        self.api.unsub({"action": "unsub", "ch": "accounts.update#1"})
        time.sleep(30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
