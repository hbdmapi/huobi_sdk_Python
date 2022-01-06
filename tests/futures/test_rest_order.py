import sys
import unittest

sys.path.append('../..')
from huobi.utils.logger import logger
from huobi.futures.rest.order import Order
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Order(ACCESS_KEY, SECRET_KEY)

    def test_order(self):
        result = self.api.order(
            {"symbol": "trx", "contract_type": "quarter", "price": 0.065, "volume": 1, "direction": "buy", "offset": "open", "lever_rate": 10, "order_price_type": "limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_batch_order(self):
        result = self.api.batch_order(
            {"orders_data":[{"symbol": "trx", "contract_type": "quarter", "price": 0.065, "volume": 1, "direction": "buy", "offset": "open", "lever_rate": 10, "order_price_type": "limit"}]})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel(self):
        result = self.api.cancel(
            {"symbol": "trx", "order_id": "928584969008689152"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_all(self):
        result = self.api.cancel_all(
            {"symbol": "trx", "direction": "buy", "offset": "open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_switch_lever_rate(self):
        result = self.api.switch_lever_rate(
            {"symbol": "trx", "lever_rate": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_info(self):
        result = self.api.get_order_info(
            {"symbol": "trx", "order_id": "928676706917883904"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_detail(self):
        result = self.api.get_order_detail(
            {"symbol": "trx", "order_id": "928676706917883904"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_open_orders(self):
        result = self.api.get_open_orders(
            {"symbol": "trx"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders(self):
        result = self.api.get_his_orders(
            {"symbol": "trx", "trade_type": 0, "type": 1, "status": "0", "create_date": 90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders_exact(self):
        result = self.api.get_his_orders_exact(
            {"symbol": "trx", "trade_type": 0, "type": 1, "status": "0"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results(self):
        result = self.api.get_match_results(
            {"symbol": "trx", "trade_type": 0, "create_date": 90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results_exact(self):
        result = self.api.get_match_results_exact(
            {"symbol": "trx", "trade_type": 0})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_lightning_close_position(self):
        result = self.api.lightning_close_position(
            {"symbol": "trx", "contract_type": "quarter", "volume": 1, "direction": "sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
