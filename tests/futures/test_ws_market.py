import sys
import unittest
import time

sys.path.append('../..')
from huobi.futures.ws.market import Market
from huobi.utils.logger import logger


class TestWsMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_sub_kline(self):
        self.api.sub({"sub": "market.BTC_CQ.kline.1min"}, lambda x: logger.info(x))
        time.sleep(10)
        
    def test_req_kline(self):
        ws = self.api.req({"req": "market.BTC_CQ.kline.1min", "from": 1641270718, "to": 1641275718}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.eth_cq.kline.15min", "from": 1641270718, "to": 1641275718})
        time.sleep(10)

    def test_sub_depth(self):
        self.api.sub({"sub": "market.BTC_CQ.depth.step0"}, lambda x: logger.info(x))
        time.sleep(10)

    def test_sub_incremental_depth(self):
        self.api.sub({"sub": "market.BTC_CQ.depth.size_20.high_freq", "data_type":"incremental"}, lambda x: logger.info(x))
        time.sleep(10)

    def test_sub_detail(self):
        self.api.sub({"sub": "market.BTC_CQ.detail"}, lambda x: logger.info(x))
        time.sleep(10)

    def test_sub_bbo(self):
        self.api.sub({"sub": "market.BTC_CQ.bbo"}, lambda x: logger.info(x))
        time.sleep(10)

    def test_req_trade_detail(self):
        ws = self.api.sub({"req": "market.BTC_CQ.trade.detail"}, lambda x: logger.info(x))
        ws.send_msg({"req": "market.BTC_CQ.trade.detail"})
        time.sleep(10)

    def test_sub_trade_detail(self):
        self.api.sub({"sub": "market.BTC_CQ.trade.detail"}, lambda x: logger.info(x))
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
