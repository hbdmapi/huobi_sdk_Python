from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class MarginAccount:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def repay(self, params: dict) -> json:
        path = "/v2/account/repayment"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def isolated_transfer_in(self, params: dict) -> json:
        path = "/v1/dw/transfer-in/margin"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def isolated_transfer_out(self, params: dict) -> json:
        path = "/v1/dw/transfer-out/margin"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def isolated_get_loan_info(self, params: dict = None) -> json:
        path = "/v1/margin/loan-info"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def isolated_orders(self, params: dict) -> json:
        path = "/v1/margin/orders"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def isolated_repay(self, params: dict) -> json:
        order_id = params['order-id']
        path = "/v1/margin/orders/{}/repay".format(order_id)
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def isolated_get_order_info(self, params: dict) -> json:
        path = "/v1/margin/loan-orders"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def isolated_get_balance(self, params: dict = None) -> json:
        path = "/v1/margin/accounts/balance"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def cross_transfer_in(self, params: dict) -> json:
        path = "/v1/cross-margin/transfer-in"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cross_transfer_out(self, params: dict) -> json:
        path = "/v1/cross-margin/transfer-out"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cross_get_loan_info(self) -> json:
        path = "/v1/cross-margin/loan-info"
        return get(self.__host, path, None, self.__access_key, self.__secret_key)

    def cross_get_hold_limit(self, params: dict) -> json:
        path = "/v2/margin/limit"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def cross_orders(self, params: dict) -> json:
        path = "/v1/cross-margin/orders"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cross_repay(self, params: dict) -> json:
        order_id = params['order-id']
        path = "/v1/cross-margin/orders/{order-id}/repay".format(order_id)
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def cross_get_order_info(self, params: dict) -> json:
        path = "/v1/cross-margin/loan-orders"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def cross_get_balance(self, params: dict = None) -> json:
        path = "/v1/cross-margin/accounts/balance"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_repayment(self, params: dict = None) -> json:
        path = "/v2/account/repayment"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    