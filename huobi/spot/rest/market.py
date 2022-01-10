from huobi.utils.http import get
from huobi.host import HOST_SPOT
import json


class Market:
    def __init__(self, host=HOST_SPOT):
        self.__host = host

    def get_kline(self, params: dict = None) -> json:
        path = "/market/history/kline"
        return get(self.__host, path, params)

    def get_merged(self, params: dict = None) -> json:
        path = "/market/detail/merged"
        return get(self.__host, path, params)

    def get_tickers(self) -> json:
        path = "/market/tickers"
        return get(self.__host, path)

    def get_depth(self, params: dict = None) -> json:
        path = "/market/depth"
        return get(self.__host, path, params)

    def get_trade(self, params: dict = None) -> json:
        path = "/market/trade"
        return get(self.__host, path, params)

    def get_his_trade(self, params: dict = None) -> json:
        path = "/market/history/trade"
        return get(self.__host, path, params)

    def get_market_detail(self, params: dict = None) -> json:
        path = "/market/detail"
        return get(self.__host, path, params)

    def get_etp(self, params: dict = None) -> json:
        path = "/market/etp"
        return get(self.__host, path, params)