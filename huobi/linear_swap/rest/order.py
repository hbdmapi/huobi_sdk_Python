from huobi.utils.http import post
from huobi.host import HOST_FUTURES
import json


class Order:
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_FUTURES):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def isolated_order(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_order(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_batch_order(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_batchorder"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_batch_order(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_batchorder"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_cancel(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_cancel(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_cancel_all(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_cancel_all(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_switch_lever_rate(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_switch_lever_rate"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_switch_lever_rate(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_switch_lever_rate"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_order_info(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_order_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_order_info(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_order_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_order_detail(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_order_detail"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_order_detail(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_order_detail"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_open_orders(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_open_orders(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_his_orders(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_his_orders(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_his_orders_exact(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_hisorders_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_his_orders_exact(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_hisorders_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_match_results(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_matchresults"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_match_results(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_matchresults"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_get_match_results_exact(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_matchresults_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_get_match_results_exact(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_matchresults_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def isolated_lightning_close_position(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_lightning_close_position"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cross_lightning_close_position(self, data: dict = None) -> json:
        path = "/linear-swap-api/v1/swap_cross_lightning_close_position"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
