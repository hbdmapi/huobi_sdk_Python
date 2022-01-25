import sys
import unittest

sys.path.append('../../src')
from tests.config import ACCESS_KEY, SECRET_KEY
from huobi.futures.rest.transfer import Transfer
from huobi.utils.logger import logger

class TestRestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Transfer(ACCESS_KEY, SECRET_KEY)

    def test_transfer(self):
        result = self.api.transfer(
            {"currency": "trx", "type": "pro-to-futures", "amount": 10})
        logger.info(result)
        self.assertEqual("ok", result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
