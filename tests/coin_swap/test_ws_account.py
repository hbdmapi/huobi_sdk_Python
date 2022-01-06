import sys
import unittest
import time

sys.path.append('../..')
from huobi.utils.logger import logger
from huobi.coin_swap.ws.account import Account
from tests.config import ACCESS_KEY, SECRET_KEY


class TestWsAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Account(ACCESS_KEY, SECRET_KEY)

    def test_sub_orders(self):
        self.api.sub({"op": "sub", "topic": "orders.btc-usd"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "orders.btc-usd"})
        time.sleep(10)

    def test_sub_accounts(self):
        self.api.sub({"op": "sub", "topic": "accounts.btc-usd"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "accounts.btc-usd"})
        time.sleep(10)

    def test_sub_positions(self):
        self.api.sub({"op": "sub", "topic": "positions.btc-usd"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "positions.btc-usd"})
        time.sleep(10)

    def test_sub_matchOrders(self):
        self.api.sub({"op": "sub", "topic": "matchOrders.btc-usd"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "matchOrders.btc-usd"})
        time.sleep(10)

    def test_sub_liquidation_orders(self):
        self.api.sub({"op": "sub", "topic": "public.*.liquidation_orders"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "public.*.liquidation_orders"})
        time.sleep(10)

    def test_sub_funding_rate(self):
        self.api.sub({"op": "sub", "topic": "public.*.funding_rate"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "public.*.funding_rate"})
        time.sleep(10)

    def test_sub_contract_info(self):
        self.api.sub({"op": "sub", "topic": "public.*.contract_info"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "public.*.contract_info"})
        time.sleep(10)

    def test_sub_trigger_order(self):
        self.api.sub({"op": "sub", "topic": "trigger_order.*"},
                     lambda x: logger.info(x))
        time.sleep(10)
        self.api.unsub({"op": "unsub", "topic": "trigger_order.*"})
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
