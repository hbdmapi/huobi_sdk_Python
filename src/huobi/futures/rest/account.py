import json

from huobi.utils.http import get, post, get_url_suffix
from huobi.host import HOST_FUTURES


class Account:
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_FUTURES):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host
    
    def get_balance_valuation(self, data: dict = None) -> json:
        path = "/api/v1/contract_balance_valuation"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
    
    def get_account_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_account_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_position_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_position_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def set_sub_auth(self, data: dict = None) -> json:
        path = "/api/v1/contract_sub_auth"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_sub_account_list(self, data: dict = None) -> json:
        path = "/api/v1/contract_sub_account_list"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_sub_account_info_list(self, data: dict = None) -> json:
        path = "/api/v1/contract_sub_account_info_list"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_sub_account_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_sub_account_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_sub_position_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_sub_position_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_financial_record(self, data: dict = None) -> json:
        path = "/api/v1/contract_financial_record"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_financial_record_exact(self, data: dict = None) -> json:
        path = "/api/v1/contract_financial_record_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_user_settlement_records(self, data: dict = None) -> json:
        path = "/api/v1/contract_user_settlement_records"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_order_limit(self, data: dict = None) -> json:
        path = "/api/v1/contract_order_limit"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_fee(self, data: dict = None) -> json:
        path = "/api/v1/contract_fee"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_transfer_limit(self, data: dict = None) -> json:
        path = "/api/v1/contract_transfer_limit"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_position_limit(self, data: dict = None) -> json:
        path = "/api/v1/contract_position_limit"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_account_position_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_account_position_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def master_sub_transfer(self, data: dict = None) -> json:
        path = "/api/v1/contract_master_sub_transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_master_sub_transfer_record(self, data: dict = None) -> json:
        path = "/api/v1/contract_master_sub_transfer_record"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_api_trading_status(self, params: dict = None) -> json:
        path = "/api/v1/contract_api_trading_status"
        path = "{}?{}".format(path, get_url_suffix('get', self.__host, path, self.__access_key, self.__secret_key))
        return get(self.__host, path)

    def get_available_level_rate(self, data: dict = None) -> json:
        path = "/api/v1/contract_available_level_rate"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
        
