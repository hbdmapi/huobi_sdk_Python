from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class AlgoOrder:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def order(self, params: dict) -> json:
        path = "/v2/algo-orders"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cancel(self, params: dict) -> json:
        path = "/v2/algo-orders/cancellation"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_open_orders(self, params: dict = None) -> json:
        path = "/v2/algo-orders/opening"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_history(self, params: dict) -> json:
        path = "/v2/algo-orders/history"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_open_or_failed_orders(self, params: dict) -> json:
        path = "/v2/algo-orders/specific"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    
