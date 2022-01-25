import sys
import unittest
import time

sys.path.append('../../src')
from huobi.utils.logger import logger
from huobi.linear_swap.ws.market import Market


class TestWsMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_sub_kline(self):
        self.api.sub({"sub": "market.BTC-USDT.kline.1min"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)
        
    def test_req_kline(self):
        ws = self.api.req({"req": "market.BTC-USDT.kline.1min", "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.eth-USDT.kline.15min", "from": 1641270718, "to": 1641275718})
        while True:
            time.sleep(1)

    def test_sub_depth(self):
        self.api.sub({"sub": "market.BTC-USDT.depth.step0"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_sub_incremental_depth(self):
        self.api.sub({"sub": "market.BTC-USDT.depth.size_20.high_freq", "data_type":"incremental"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_sub_detail(self):
        self.api.sub({"sub": "market.BTC-USDT.detail"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_sub_bbo(self):
        self.api.sub({"sub": "market.BTC-USDT.bbo"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)

    def test_req_trade_detail(self):
        ws = self.api.sub({"req": "market.BTC-USDT.trade.detail"}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.BTC-USDT.trade.detail"})
        while True:
            time.sleep(1)

    def test_sub_trade_detail(self):
        self.api.sub({"sub": "market.BTC-USDT.trade.detail"}, lambda x: logger.info(x))
        while True:
            time.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
