from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class SubUser:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def set_deduct_mode(self, params: dict = None) -> json:
        path = "/v2/sub-user/deduct-mode"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_api_key_info(self, params: dict = None) -> json:
        path = "/v2/user/api-key"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_uid(self) -> json:
        path = "/v2/user/uid"
        return get(self.__host, path, None, self.__access_key, self.__secret_key)

    def create(self, params: dict = None) -> json:
        path = "/v2/sub-user/creation"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_sub_user_list(self, params: dict = None) -> json:
        path = "/v2/sub-user/user-list"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def management(self, params: dict = None) -> json:
        path = "/v2/sub-user/management"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_state(self, params: dict = None) -> json:
        path = "/v2/sub-user/user-state"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def set_tradable(self, params: dict = None) -> json:
        path = "/v2/sub-user/tradable-market"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def set_transferability(self, params: dict = None) -> json:
        path = "/v2/sub-user/transferability"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_account_list(self, params: dict = None) -> json:
        path = "/v2/sub-user/account-list"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def generate_api_key(self, params: dict = None) -> json:
        path = "/v2/sub-user/api-key-generation"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def modify_api_key(self, params: dict = None) -> json:
        path = "/v2/sub-user/api-key-modification"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def delete_api_key(self, params: dict = None) -> json:
        path = "/v2/sub-user/api-key-deletion"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def transfer(self, params: dict = None) -> json:
        path = "/v1/subuser/transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)

    def get_deposit_address(self, params: dict = None) -> json:
        path = "/v2/sub-user/deposit-address"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_deposit(self, params: dict = None) -> json:
        path = "/v2/sub-user/query-deposit"
        return get(self.__host, path, params, self.__access_key, self.__secret_key)

    def get_aggregate_balance(self) -> json:
        path = "/v1/subuser/aggregate-balance"
        return get(self.__host, path, None, self.__access_key, self.__secret_key)

    def get_balance(self, params: dict = None) -> json:
        sub_uid = params['sub-uid']
        path = "/v1/account/accounts/{}".format(sub_uid)
        return get(self.__host, path, params, self.__access_key, self.__secret_key)
