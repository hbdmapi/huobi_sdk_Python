from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class Order:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def order(self, params: dict = None) -> json:
        path = "/v1/order/orders/place"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def batch_orders(self, params: list = None) -> json:
        path = "/v1/order/batch-orders"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cancel_by_id(self, params: dict = None) -> json:
        order_id = params['order-id']
        path = "/v1/order/orders/{}/submitcancel".format(order_id)
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cancel_by_cid(self, params: dict = None) -> json:
        path = "/v1/order/orders/submitCancelClientOrder"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cancel_all_after(self, params: dict = None) -> json:
        path = "/v2/algo-orders/cancel-all-after"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_open_orders(self, params: dict = None) -> json:
        path = "/v1/order/openOrders"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def batch_cancel_by_cri(self, params: dict = None) -> json:
        path = "/v1/order/orders/batchCancelOpenOrders"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def batch_cancel_by_ids(self, params: dict = None) -> json:
        path = "/v1/order/orders/batchcancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_order_detail_by_id(self, params: dict = None) -> json:
        order_id = params['order-id']
        path = "/v1/order/orders/{}".format(order_id)
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_order_detail_by_cid(self, params: dict = None) -> json:
        path = "/v1/order/orders/getClientOrder"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_match_results_by_id(self, params: dict = None) -> json:
        order_id = params['order-id']
        path = "/v1/order/orders/{}/matchresults".format(order_id)
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_orders(self, params: dict = None) -> json:
        path = "/v1/order/orders"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_history(self, params: dict = None) -> json:
        path = "/v1/order/history"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_match_results_by_cri(self, params: dict = None) -> json:
        path = "/v1/order/matchresults"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_fee_rate(self, params: dict = None) -> json:
        path = "/v2/reference/transact-fee-rate"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)
