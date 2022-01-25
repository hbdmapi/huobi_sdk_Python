import sys
import unittest

sys.path.append('../../src')
from huobi.utils.logger import logger
from huobi.coin_swap.rest.order import Order
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Order(ACCESS_KEY, SECRET_KEY)

    def test_order(self):
        result = self.api.order(
            {"contract_code": "trx-usd", "price": 0.065, "volume": 1, "direction": "buy", "offset": "open", "lever_rate": 10, "order_price_type": "limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_batch_order(self):
        result = self.api.batch_order(
            {"orders_data":[{"contract_code": "trx-usd", "price": 0.065, "volume": 1, "direction": "buy", "offset": "open", "lever_rate": 10, "order_price_type": "limit"}]})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel(self):
        result = self.api.cancel(
            {"contract_code": "trx-usd", "order_id": "928584969008689152"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_all(self):
        result = self.api.cancel_all(
            {"contract_code": "trx-usd", "direction": "buy", "offset": "open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_switch_lever_rate(self):
        result = self.api.switch_lever_rate(
            {"contract_code": "trx-usd", "lever_rate": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_info(self):
        result = self.api.get_order_info(
            {"contract_code": "trx-usd", "order_id": "928584969008689152"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_detail(self):
        result = self.api.get_order_detail(
            {"contract_code": "trx-usd", "order_id": "928584969008689152"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_open_orders(self):
        result = self.api.get_open_orders(
            {"contract_code": "trx-usd"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders(self):
        result = self.api.get_his_orders(
            {"contract_code": "trx-usd", "trade_type": 0, "type": 1, "status": "0", "create_date": 90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders_exact(self):
        result = self.api.get_his_orders_exact(
            {"contract_code": "trx-usd", "trade_type": 0, "type": 1, "status": "0"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results(self):
        result = self.api.get_match_results(
            {"contract_code": "trx-usd", "trade_type": 0, "create_date": 90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results_exact(self):
        result = self.api.get_match_results_exact(
            {"contract_code": "trx-usd", "trade_type": 0})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_lightning_close_position(self):
        result = self.api.lightning_close_position(
            {"contract_code": "trx-usd", "volume": 1, "direction": "sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
