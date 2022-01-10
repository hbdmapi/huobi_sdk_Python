import sys
import unittest

sys.path.append('../..')
from huobi.spot.rest.account import Account
from huobi.utils.logger import logger
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Account(ACCESS_KEY, SECRET_KEY)

    def test_get_accounts(self):
        result = self.api.get_accounts()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_balance(self):
        result = self.api.get_balance({'account-id': '38788389'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_valuation(self):
        result = self.api.get_valuation(
            {'accountType': '1', 'valuationCurrency': 'BTC'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_uid_valuation(self):
        result = self.api.get_uid_valuation(
            {'accountType': '1', 'valuationCurrency': 'BTC', 'subUid': '38788389'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_account_transfer(self):
        result = self.api.account_transfer(
            {'from-user': '38788389', 'from-account-type': 'spot', 'from-account': '1',
             'to-user': '38788389', 'to-account-type': 'spot', 'to-account': '1',
             'currency': 'trx', 'amount': '10'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_account_history(self):
        result = self.api.get_account_history({'account-id': '38788389'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_ledger(self):
        result = self.api.get_ledger({'accountId': '38788389'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_futures_transfer(self):
        result = self.api.futures_transfer(
            {'currency': 'trx', 'amount': 10, 'type': 'pro-to-futures'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_point(self):
        result = self.api.get_point({'subUid': '38788389'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_point_transfer(self):
        result = self.api.point_transfer(
            {'fromUid': '38788389', 'toUid': '1', 'groupId': 1, 'amount': 10})
        logger.info(result)
        self.assertEqual(200, result['code'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
