import sys
import unittest

sys.path.append('../../src')
from tests.config import ACCESS_KEY, SECRET_KEY
from huobi.coin_swap.rest.transfer import Transfer
from huobi.utils.logger import logger

class TestRestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Transfer(ACCESS_KEY, SECRET_KEY)

    def test_transfer(self):
        result = self.api.transfer(
            {"from": "swap", "to": "spot", "currency": "trx", "amount": 10})
        logger.info(result)
        self.assertEqual(True, result['success'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
