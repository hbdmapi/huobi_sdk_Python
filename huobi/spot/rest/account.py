from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class Account:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def get_accounts(self) -> json:
        path = "/v1/account/accounts"
        return get(self.__host, path, None, self.__access_key, self.__secret_key)

    def get_balance(self, params: dict) -> json:
        path = "/v1/account/accounts/{}/balance".format(params['account-id'])
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_valuation(self, params: dict = None) -> json:
        path = "/v2/account/valuation"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_type_valuation(self, params: dict) -> json:
        path = "/v2/account/asset-valuation"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def account_transfer(self, params: dict) -> json:
        path = "/v1/account/transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_history(self, params: dict) -> json:
        path = "/v1/account/history"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_ledger(self, params: dict) -> json:
        path = "/v2/account/ledger"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def futures_transfer(self, params: dict) -> json:
        path = "/v1/futures/transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_point(self, params: dict = None) -> json:
        path = "/v2/point/account"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def point_transfer(self, params: dict) -> json:
        path = "/v2/point/transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)
