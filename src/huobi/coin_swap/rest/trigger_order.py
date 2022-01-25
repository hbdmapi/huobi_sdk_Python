import json

from huobi.utils.http import post
from huobi.host import HOST_FUTURES


class TriggerOrder:
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_FUTURES):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def order(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_trigger_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cancel(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_trigger_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cancel_all(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_trigger_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_open_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_trigger_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_his_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_trigger_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def tpsl_order(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_tpsl_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def tpsl_cancel(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_tpsl_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def tpsl_cancel_all(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_tpsl_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_tpsl_open_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_tpsl_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_tpsl_his_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_tpsl_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_relation_tpsl_order(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_relation_tpsl_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
        
    def track_order(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_track_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def track_cancel(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_track_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def track_cancel_all(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_track_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_track_open_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_track_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_track_his_orders(self, data: dict = None) -> json:
        path = "/swap-api/v1/swap_track_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
