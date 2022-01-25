from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class Etp:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def order(self, params: dict) -> json:
        path = "/v2/etp/creation"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def redeem(self, params: dict) -> json:
        path = "/v2/etp/redemption"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_transactions(self, params: dict) -> json:
        path = "/v2/etp/transactions"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_transaction_by_id(self, params: dict) -> json:
        path = "/v2/etp/transaction"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_rebalance(self, params: dict) -> json:
        path = "/v2/etp/rebalance"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def cancel(self, params: dict) -> json:
        transact_id = params['transactId']
        path = "/v2/etp/{}/cancel".format(transact_id)
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def batch_cancel(self, params: dict) -> json:
        path = "/v2/etp/batch-cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_hold_limit(self, params: dict) -> json:
        path = "/v2/etp/limit"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)
