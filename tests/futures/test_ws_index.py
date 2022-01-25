import sys
import unittest
import time

sys.path.append('../../src')
from huobi.futures.ws.index import Index
from huobi.utils.logger import logger


class TestWsIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Index()

    def test_sub_index(self):
        self.api.sub({"sub": "market.BTC_CQ.index.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_index(self):
        ws = self.api.req({"req": "market.BTC_CQ.index.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH_CQ.index.1min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_basis(self):
        self.api.sub({"sub": "market.BTC_CQ.basis.1min.open"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_basis(self):
        ws = self.api.req({"req": "market.BTC_CQ.basis.1min.open",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH_CQ.basis.1min.open",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_mark_price(self):
        self.api.sub({"sub": "market.BTC_CQ.mark_price.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_mark_price(self):
        ws = self.api.req({"req": "market.BTC_CQ.mark_price.5min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH_CQ.mark_price.5min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
