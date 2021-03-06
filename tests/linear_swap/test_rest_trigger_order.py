import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from huobi.utils.logger import logger
from huobi.linear_swap.rest.trigger_order import TriggerOrder
from config import ACCESS_KEY, SECRET_KEY


class TestRestTriggerOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TriggerOrder(ACCESS_KEY, SECRET_KEY)
    
    def test_isolated_order(self):
        result = self.api.isolated_order(
            {"contract_code": "eos-usdt", "trigger_type":"le", "trigger_price":3, "order_price":3, "volume":1, "direction":"buy", "offset":"open", "lever_rate":10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_order(self):
        result = self.api.cross_order(
            {"contract_code": "eos-usdt", "trigger_type":"le", "trigger_price":3, "order_price":3, "volume":1, "direction":"buy", "offset":"open", "lever_rate":10})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_cancel(self):
        result = self.api.isolated_cancel(
            {"contract_code": "eos-usdt", "order_id":"926494484492673024"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_cancel(self):
        result = self.api.cross_cancel(
            {"contract_code": "eos-usdt", "order_id":"926494666180870144"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_cancel_all(self):
        result = self.api.isolated_cancel_all(
            {"contract_code": "eos-usdt", "direction":"buy", "offset":"open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_cancel_all(self):
        result = self.api.cross_cancel_all(
            {"contract_code": "eos-usdt", "direction":"buy", "offset":"open"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_get_open_orders(self):
        result = self.api.isolated_get_open_orders(
            {"contract_code": "eos-usdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_get_open_orders(self):
        result = self.api.cross_get_open_orders(
            {"contract_code": "eos-usdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_get_his_orders(self):
        result = self.api.isolated_get_his_orders(
            {"contract_code": "eos-usdt", "trade_type":0, "status":"0", "create_date":90, "sort_by":"created_at"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_get_his_orders(self):
        result = self.api.cross_get_his_orders(
            {"contract_code": "eos-usdt", "trade_type":0, "status":"0", "create_date":90, "sort_by":"created_at"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_tpsl_order(self):
        result = self.api.isolated_tpsl_order(
            {"contract_code": "eos-usdt", "direction":"sell", "volume":1, "tp_trigger_price":5, "tp_order_price":5, "tp_order_price_type":"limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_tpsl_order(self):
        result = self.api.cross_tpsl_order(
            {"contract_code": "eos-usdt", "direction":"sell", "volume":1, "sl_trigger_price":2, "sl_order_price":2, "sl_order_price_type":"limit"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_tpsl_cancel(self):
        result = self.api.isolated_tpsl_cancel(
            {"contract_code": "eos-usdt", "order_id":"813734657874460672"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_tpsl_cancel(self):
        result = self.api.cross_tpsl_cancel(
            {"contract_code": "eos-usdt", "order_id":"813735137312677889"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_tpsl_cancel_all(self):
        result = self.api.isolated_tpsl_cancel_all(
            {"contract_code": "eos-usdt", "direction":"sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_tpsl_cancel_all(self):
        result = self.api.cross_tpsl_cancel_all(
            {"contract_code": "eos-usdt", "direction":"sell"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_get_tpsl_open_orders(self):
        result = self.api.isolated_get_tpsl_open_orders(
            {"contract_code": "eos-usdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_get_tpsl_open_orders(self):
        result = self.api.cross_get_tpsl_open_orders(
            {"contract_code": "eos-usdt"})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_get_tpsl_his_orders(self):
        result = self.api.isolated_get_tpsl_his_orders(
            {"contract_code": "eos-usdt", "status":"0", "create_date":90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_get_tpsl_his_orders(self):
        result = self.api.cross_get_tpsl_his_orders(
            {"contract_code": "eos-usdt", "status":"0", "create_date":90})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_isolated_get_relation_tpsl_order(self):
        result = self.api.isolated_get_relation_tpsl_order(
            {"contract_code": "eos-usdt", "order_id":""})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_cross_get_relation_tpsl_order(self):
        result = self.api.cross_get_relation_tpsl_order(
            {"contract_code": "eos-usdt", "order_id":""})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
