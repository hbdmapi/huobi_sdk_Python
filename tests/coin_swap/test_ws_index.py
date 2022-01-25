import sys
import unittest
import time

sys.path.append('../../src')
from huobi.coin_swap.ws.index import Index
from huobi.utils.logger import logger


class TestWsIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Index()

    def test_sub_index(self):
        self.api.sub({"sub": "market.BTC-USD.index.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_index(self):
        ws = self.api.req({"req": "market.BTC-USD.index.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USD.index.1min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_premium_index(self):
        self.api.sub({"sub": "market.BTC-USD.premium_index.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_premium_index(self):
        ws = self.api.req({"req": "market.BTC-USD.premium_index.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USD.premium_index.1min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_estimated_rate(self):
        self.api.sub({"sub": "market.BTC-USD.estimated_rate.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_estimated_rate(self):
        ws = self.api.req({"req": "market.BTC-USD.estimated_rate.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USD.estimated_rate.1min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_basis(self):
        self.api.sub({"sub": "market.BTC-USD.basis.1min.open"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_basis(self):
        ws = self.api.req({"req": "market.BTC-USD.basis.1min.open",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USD.basis.1min.open",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_mark_price(self):
        self.api.sub({"sub": "market.BTC-USD.mark_price.1min"},
                     lambda x: logger.info(x))
        time.sleep(10)

    def test_req_mark_price(self):
        ws = self.api.req({"req": "market.BTC-USD.mark_price.5min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USD.mark_price.5min",
                     "from": 1641270718, "to": 1641275718})
        time.sleep(10)



if __name__ == '__main__':
    unittest.main(verbosity=2)
