import sys
import unittest
import time

sys.path.append('../../src')
from huobi.utils.logger import logger
from huobi.spot.ws.market import Market


class TestWsMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_sub_kline(self):
        ws = self.api.sub({"sub": "market.btcusdt.kline.1min"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_ticker(self):
        ws = self.api.sub({"sub": "market.btcusdt.ticker"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_depth(self):
        ws = self.api.sub({"sub": "market.btcusdt.depth.step0"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_mbp_incremental(self):
        ws = self.api.sub_mbp({"sub": "market.btcusdt.mbp.150"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_mbp_full(self):
        ws = self.api.sub({"sub": "market.btcusdt.mbp.refresh.20"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_bbo(self):
        ws = self.api.sub({"sub": "market.btcusdt.bbo"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_trade_detail(self):
        ws = self.api.sub({"sub": "market.btcusdt.trade.detail"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_detail(self):
        ws = self.api.sub({"sub": "market.btcusdt.detail"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()

    def test_sub_etp(self):
        ws = self.api.sub({"sub": "market.btc3lusdt.etp"}, lambda x: logger.info(x))
        time.sleep(10)
        ws.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
