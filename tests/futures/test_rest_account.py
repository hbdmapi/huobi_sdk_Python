import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from huobi.utils.logger import logger
from huobi.futures.rest.account import Account
from config import ACCESS_KEY, SECRET_KEY


class TestRestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Account(ACCESS_KEY, SECRET_KEY)

    def test_get_balance_valuation(self):
        result = self.api.get_balance_valuation(
            {"valuation_asset": "usd"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_account_info(self):
        result = self.api.get_account_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_position_info(self):
        result = self.api.get_position_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_set_sub_auth(self):
        result = self.api.set_sub_auth(
            {"sub_uid": "300540322", "sub_auth": 1})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_sub_account_list(self):
        result = self.api.get_sub_account_list(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_sub_account_info_list(self):
        result = self.api.get_sub_account_info_list(
            {"symbol": "btc", "page_index": 1, "page_size": 20})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_sub_account_info(self):
        result = self.api.get_sub_account_info(
            {"symbol": "btc", "sub_uid": "300540322"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_sub_position_info(self):
        result = self.api.get_sub_position_info(
            {"symbol": "btc", "sub_uid": "300540322"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_financial_record(self):
        result = self.api.get_financial_record(
            {"symbol": "usd", "symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_financial_record_exact(self):
        result = self.api.get_financial_record_exact(
            {"symbol": "usd", "symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_user_settlement_records(self):
        result = self.api.get_user_settlement_records(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_limit(self):
        result = self.api.get_order_limit(
            {"symbol": "btc", "order_price_type": "limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_fee(self):
        result = self.api.get_fee(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_transfer_limit(self):
        result = self.api.get_transfer_limit(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_position_limit(self):
        result = self.api.get_position_limit(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_account_position_info(self):
        result = self.api.get_account_position_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_master_sub_transfer(self):
        result = self.api.master_sub_transfer(
            {"sub_uid": 300540322, "symbol": "btc", "amount": 1, "type": "master_to_sub"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_master_sub_transfer_record(self):
        result = self.api.get_master_sub_transfer_record(
            {"symbol": "btc", "create_date": 90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_api_trading_status(self):
        result = self.api.get_api_trading_status()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_available_level_rate(self):
        result = self.api.get_available_level_rate(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
