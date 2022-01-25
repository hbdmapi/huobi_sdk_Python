import sys
import unittest

sys.path.append('../../src')
from huobi.spot.rest.order import Order
from huobi.utils.logger import logger
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Order(ACCESS_KEY, SECRET_KEY)

    def test_order(self):
        result = self.api.order({
            "account-id": "38788389",
            "amount": "100",
            "price": "0.06",
            "source": "api",
            "symbol": "trxusdt",
            "type": "buy-limit",
            "client-order-id": "a0001"
        })
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_batch_orders(self):
        result = self.api.batch_orders([{
            "account-id": "38788389",
            "amount": "100",
            "price": "0.06",
            "source": "api",
            "symbol": "trxusdt",
            "type": "buy-limit",
            "client-order-id": "a0002"
        }])
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_by_id(self):
        result = self.api.cancel_by_id({"order-id": "452714856530521"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_by_cid(self):
        result = self.api.cancel_by_cid({"client-order-id": "a0001"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_all_after(self):
        result = self.api.cancel_all_after({"timeout": 5})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_open_orders(self):
        result = self.api.get_open_orders({"symbol": "trxusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_batch_cancel_by_cri(self):
        result = self.api.batch_cancel_by_cri({"symbol": "trxusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_batch_cancel_by_ids(self):
        result = self.api.batch_cancel_by_ids(
            {"order-ids": ["452713824238173"]})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_detail_by_id(self):
        result = self.api.get_order_detail_by_id({"order-id": "452713824238173"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_order_detail_by_cid(self):
        result = self.api.get_order_detail_by_cid({"clientOrderId": "a0002"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results_by_id(self):
        result = self.api.get_match_results_by_id({"order-id": "452713824238173"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_orders(self):
        result = self.api.get_orders(
            {"symbol": "trxusdt", "states": "canceled"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_history(self):
        result = self.api.get_history({"symbol": "trxusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_match_results_by_cri(self):
        result = self.api.get_match_results_by_cri({"symbol": "trxusdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_fee_rate(self):
        result = self.api.get_fee_rate({"symbols": "trxusdt"})
        logger.info(result)
        self.assertEqual(200, result['code'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
