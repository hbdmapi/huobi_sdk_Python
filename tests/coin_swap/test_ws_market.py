import sys
import unittest
import time

sys.path.append('../..')
from huobi.utils.logger import logger
from huobi.coin_swap.ws.market import Market


class TestWsMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_sub_kline(self):
        self.api.sub({"sub": "market.BTC-USD.kline.1min"}, lambda x: logger.info(x))
        time.sleep(30)
        
    def test_req_kline(self):
        ws = self.api.req({"req": "market.BTC-USD.kline.1min", "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.eth-usd.kline.15min", "from": 1641270718, "to": 1641275718})
        time.sleep(30)

    def test_sub_depth(self):
        self.api.sub({"sub": "market.BTC-USD.depth.step0"}, lambda x: logger.info(x))
        time.sleep(30)

    def test_sub_incremental_depth(self):
        self.api.sub({"sub": "market.BTC-USD.depth.size_20.high_freq", "data_type":"incremental"}, lambda x: logger.info(x))
        time.sleep(30)

    def test_sub_detail(self):
        self.api.sub({"sub": "market.BTC-USD.detail"}, lambda x: logger.info(x))
        time.sleep(30)

    def test_sub_bbo(self):
        self.api.sub({"sub": "market.BTC-USD.bbo"}, lambda x: logger.info(x))
        time.sleep(30)

    def test_req_trade_detail(self):
        ws = self.api.sub({"req": "market.BTC-USD.trade.detail"}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.BTC-USD.trade.detail"})
        time.sleep(30)

    def test_sub_trade_detail(self):
        self.api.sub({"sub": "market.BTC-USD.trade.detail"}, lambda x: logger.info(x))
        time.sleep(30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
