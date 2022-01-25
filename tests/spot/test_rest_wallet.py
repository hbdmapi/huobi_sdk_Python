import sys
import unittest

sys.path.append('../../src')
from huobi.spot.rest.wallet import Wallet
from huobi.utils.logger import logger
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestWallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Wallet(ACCESS_KEY, SECRET_KEY)

    def test_get_deposit_address(self):
        result = self.api.get_deposit_address({'currency': 'usdt'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_withdraw_quota(self):
        result = self.api.get_withdraw_quota({'currency': 'usdt'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_withdraw_address(self):
        result = self.api.get_withdraw_address({'currency': 'usdt'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_withdraw(self):
        result = self.api.withdraw(
            {'address': 'usdt', 'amount': '10', 'currency': 'usdt', 'fee': '2'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_withdraw_info(self):
        result = self.api.get_withdraw_info({'clientOrderId': 'usdt'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel(self):
        result = self.api.cancel({'withdraw-id': 'usdt'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_deposit_withdraw_info(self):
        result = self.api.get_deposit_withdraw_info({'type': 'deposit'})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
