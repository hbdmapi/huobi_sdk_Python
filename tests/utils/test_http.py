import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from config import ACCESS_KEY, SECRET_KEY
from huobi.host import HOST_FUTURES
from huobi.utils.logger import logger
from huobi.utils.http import get, post

class TestHttp(unittest.TestCase):
    def test_get(self):
        result = get(HOST_FUTURES, '/linear-swap-api/v1/swap_contract_info',
                     {'contract_code': 'BTC-USDT'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_post(self):
        result = post(HOST_FUTURES, '/linear-swap-api/v1/swap_cross_account_info',
                      ACCESS_KEY, SECRET_KEY, {'margin_account': 'USDT'})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
