import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from huobi.utils.logger import logger
from huobi.coin_swap.rest.trigger_order import TriggerOrder
from config import ACCESS_KEY, SECRET_KEY


class TestRestTriggerOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TriggerOrder(ACCESS_KEY, SECRET_KEY)
    
    def test_order(self):
        result = self.api.order(
            {"contract_code": "trx-usd", "trigger_type":"le", "trigger_price":0.065, "order_price":0.065, "volume":1, "direction":"buy", "offset":"open", "lever_rate":10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel(self):
        result = self.api.cancel(
            {"contract_code": "trx-usd", "order_id":"926494484492673024"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cancel_all(self):
        result = self.api.cancel_all(
            {"contract_code": "trx-usd", "direction":"buy", "offset":"open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_open_orders(self):
        result = self.api.get_open_orders(
            {"contract_code": "trx-usd"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_his_orders(self):
        result = self.api.get_his_orders(
            {"contract_code": "trx-usd", "trade_type":0, "status":"0", "create_date":90, "sort_by":"created_at"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_order(self):
        result = self.api.tpsl_order(
            {"contract_code": "trx-usd", "direction":"sell", "volume":1, "tp_trigger_price":0.065, "tp_order_price":0.065, "tp_order_price_type":"limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_cancel(self):
        result = self.api.tpsl_cancel(
            {"contract_code": "trx-usd", "order_id":"813734657874460672"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_tpsl_cancel_all(self):
        result = self.api.tpsl_cancel_all(
            {"contract_code": "trx-usd", "direction":"sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_tpsl_open_orders(self):
        result = self.api.get_tpsl_open_orders(
            {"contract_code": "trx-usd"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_tpsl_his_orders(self):
        result = self.api.get_tpsl_his_orders(
            {"contract_code": "trx-usd", "status":"0", "create_date":90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_relation_tpsl_order(self):
        result = self.api.get_relation_tpsl_order(
            {"contract_code": "trx-usd", "order_id":""})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
