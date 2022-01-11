from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class Wallet:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def get_deposit_address(self, params: dict = None) -> json:
        path = "/v2/account/deposit/address"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_withdraw_quota(self, params: dict = None) -> json:
        path = "/v2/account/withdraw/quota"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_withdraw_address(self, params: dict = None) -> json:
        path = "/v2/account/withdraw/address"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def withdraw(self, params: dict = None) -> json:
        path = "/v1/dw/withdraw/api/create"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_withdraw_info(self, params: dict = None) -> json:
        path = "/v1/query/withdraw/client-order-id"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def cancel(self, params: dict = None) -> json:
        withdraw_id = params['withdraw-id']
        path = "/v1/dw/withdraw-virtual/{}/cancel".format(withdraw_id)
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_deposit_withdraw_info(self, params: dict = None) -> json:
        path = "/v1/query/deposit-withdraw"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)
