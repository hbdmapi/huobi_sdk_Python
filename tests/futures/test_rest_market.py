import sys
import unittest

sys.path.append('../../src')
from huobi.futures.rest.market import Market
from huobi.utils.logger import logger

class TestRestMarket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Market()

    def test_get_contract_info(self):
        result = self.api.get_contract_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_index_info(self):
        result = self.api.get_index_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_price_limit(self):
        result = self.api.get_price_limit(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_open_interest(self):
        result = self.api.get_open_interest(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_delivery_price(self):
        result = self.api.get_delivery_price(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_estimated_settlement_price(self):
        result = self.api.get_estimated_settlement_price(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_api_state(self):
        result = self.api.get_api_state(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_depth(self):
        result = self.api.get_depth(
            {"symbol": "btc_cq", "type": "step0"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_bbo(self):
        result = self.api.get_bbo(
            {"symbol": "btc_cq"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_kline(self):
        result = self.api.get_kline(
            {"symbol": "btc_cq", "period": "1min", "size": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_mark_price_kline(self):
        result = self.api.get_mark_price_kline(
            {"symbol": "btc_cq", "period": "1min", "size": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_merged(self):
        result = self.api.get_merged(
            {"symbol": "btc_cq"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_batch_merged(self):
        result = self.api.get_batch_merged(
            {"symbol": "btc_cq"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_trade(self):
        result = self.api.get_trade(
            {"symbol": "btc_cq"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_history_trade(self):
        result = self.api.get_history_trade(
            {"symbol": "btc_cq", "size": 2000})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_risk_info(self):
        result = self.api.get_risk_info(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_insurance_fund(self):
        result = self.api.get_insurance_fund(
            {"symbol": "btc", "page_index": 2, "page_size": 100})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_adjustfactor(self):
        result = self.api.get_adjustfactor(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_open_interest(self):
        result = self.api.get_open_interest(
            {"symbol": "btc", "period": "60min", "size": 100, "amount_type": 1})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_ladder_margin(self):
        result = self.api.get_ladder_margin(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_elite_account_ratio(self):
        result = self.api.get_elite_account_ratio(
            {"symbol": "btc", "period": "5min"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_elite_position_ratio(self):
        result = self.api.get_elite_position_ratio(
            {"symbol": "btc", "period": "5min"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_liquidation_orders(self):
        result = self.api.get_liquidation_orders(
            {"symbol": "btc", "trade_type": 0, "create_date": 90, "page_index": 2, "page_size": 50})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_settlement_records(self):
        result = self.api.get_settlement_records(
            {"symbol": "btc"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_index_kline(self):
        result = self.api.get_index_kline(
            {"symbol": "btc-usd", "period": "1min", "size": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_basis(self):
        result = self.api.get_basis(
            {"symbol": "btc_cq", "period": "1min", "basis_price_type": "close", "size": 100})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
