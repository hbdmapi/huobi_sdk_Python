import sys
import unittest
import time

sys.path.append('../../src')
sys.path.append('../')
from config import ACCESS_KEY, SECRET_KEY
from huobi.utils.ws import Ws
from huobi.utils.logger import logger
from huobi.host import HOST_FUTURES


class TestWs(unittest.TestCase):

    def __callback_fun(self, jdata):
        logger.info(jdata)

    def test_sub(self):
        instance = Ws(HOST_FUTURES, "/linear-swap-ws",
                      {"sub": "market.BTC-USDT.kline.1min"}, self.__callback_fun)
        instance.connect()
        time.sleep(10)
        instance.close()
        time.sleep(10)

        instance = Ws(HOST_FUTURES, "/linear-swap-notification",
                      {"op": "sub", "topic": "accounts_cross.USDT"}, self.__callback_fun,
                      ACCESS_KEY, SECRET_KEY)
        instance.connect()
        time.sleep(10)
        instance.close()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
