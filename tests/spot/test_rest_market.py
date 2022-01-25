import sys
import unittest

sys.path.append('../../src')
from huobi.spot.rest.market import Market
from huobi.utils.logger import logger


class TestRestMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_get_kline(self):
        result = self.api.get_kline(
            {'symbol': 'btcusdt', 'period': '15min', 'size': '10'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_merged(self):
        result = self.api.get_merged({'symbol': 'btcusdt'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_tickers(self):
        result = self.api.get_tickers()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_depth(self):
        result = self.api.get_depth(
            {"symbol": "btcusdt", "depth": 5, "type": "step0"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_trade(self):
        result = self.api.get_trade({'symbol': 'btcusdt'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_trade(self):
        result = self.api.get_his_trade({'symbol': 'btcusdt', 'size': 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_market_detail(self):
        result = self.api.get_market_detail({"symbol": "btcusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_etp(self):
        result = self.api.get_etp({"symbol": "btcusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
