import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from huobi.utils.logger import logger
from huobi.futures.rest.trigger_order import TriggerOrder
from config import ACCESS_KEY, SECRET_KEY


class TestRestTriggerOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TriggerOrder(ACCESS_KEY, SECRET_KEY)
    
    def test_order(self):
        result = self.api.order(
            {"symbol": "trx", "contract_type": "quarter", "trigger_type": "le", "trigger_price": 0.065, "order_price": 0.065, "volume": 1, "direction": "buy", "offset": "open", "lever_rate": 10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel(self):
        result = self.api.cancel(
            {"symbol": "trx", "order_id":"928681980722401280"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_all(self):
        result = self.api.cancel_all(
            {"symbol": "trx", "direction":"buy", "offset":"open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_open_orders(self):
        result = self.api.get_open_orders(
            {"symbol": "trx"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders(self):
        result = self.api.get_his_orders(
            {"symbol": "trx", "trade_type":0, "status":"0", "create_date":90, "sort_by":"created_at"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_order(self):
        result = self.api.tpsl_order(
            {"symbol": "trx", "contract_type": "quarter", "direction":"sell", "volume":1, "tp_trigger_price":0.073, "tp_order_price":0.073, "tp_order_price_type":"limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_cancel(self):
        result = self.api.tpsl_cancel(
            {"symbol": "trx", "order_id":"1641456680750"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_cancel_all(self):
        result = self.api.tpsl_cancel_all(
            {"symbol": "trx", "direction":"sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_tpsl_open_orders(self):
        result = self.api.get_tpsl_open_orders(
            {"symbol": "trx"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_tpsl_his_orders(self):
        result = self.api.get_tpsl_his_orders(
            {"symbol": "trx", "status":"0", "create_date":90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_relation_tpsl_order(self):
        result = self.api.get_relation_tpsl_order(
            {"symbol": "trx", "order_id":""})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
