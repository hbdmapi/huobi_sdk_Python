import sys
import unittest

sys.path.append('../../src')
sys.path.append('../')
from config import ACCESS_KEY, SECRET_KEY
from huobi.linear_swap.rest.transfer import Transfer
from utils.logger import logger

class TestRestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Transfer(ACCESS_KEY, SECRET_KEY)

    def test_transfer(self):
        result = self.api.transfer(
            {"from": "linear-swap", "to": "spot", "currency": "usdt", "amount": 5, "margin-account": "usdt"})
        logger.info(result)
        self.assertEqual(True, result['success'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
