import sys
import unittest

sys.path.append('../..')
from huobi.spot.rest.common import Common
from huobi.utils.logger import logger


class TestRestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Common()

    def test_get_market_status(self):
        result = self.api.get_market_status()
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_symbols(self):
        result = self.api.get_symbols()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_currencys(self):
        result = self.api.get_currencys()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_chains(self):
        result = self.api.get_chains(
            {"currency": "btc", "authorizedUser": "true"})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_depth(self):
        result = self.api.get_system_time()
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
