import sys
import unittest
import time

sys.path.append('../..')
from huobi.linear_swap.ws.index import Index
from huobi.utils.logger import logger


class TestWsIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Index()

    def test_sub_index(self):
        self.api.sub({"sub": "market.BTC-USDT.index.1min"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_index(self):
        ws = self.api.req({"req": "market.btc-usdt.index.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.eth-usdt.index.1min",
                     "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)

    def test_sub_premium_index(self):
        self.api.sub({"sub": "market.BTC-USDT.premium_index.1min"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_premium_index(self):
        ws = self.api.req({"req": "market.BTC-USDT.premium_index.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USDT.premium_index.1min",
                     "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)

    def test_sub_estimated_rate(self):
        self.api.sub({"sub": "market.btc-usdt.estimated_rate.1min"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_estimated_rate(self):
        ws = self.api.req({"req": "market.BTC-USDT.estimated_rate.1min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USDT.estimated_rate.1min",
                     "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)

    def test_sub_basis(self):
        self.api.sub({"sub": "market.BTC-USDT.basis.1min.open"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_basis(self):
        ws = self.api.req({"req": "market.btc-usdt.basis.1min.open",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.eth-usdt.basis.1min.open",
                     "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)

    def test_sub_mark_price(self):
        self.api.sub({"sub": "market.BTC-USDT.mark_price.1min"},
                     lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_mark_price(self):
        ws = self.api.req({"req": "market.BTC-USDT.mark_price.5min",
                           "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.ETH-USDT.mark_price.5min",
                     "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)



if __name__ == '__main__':
    unittest.main(verbosity=2)
