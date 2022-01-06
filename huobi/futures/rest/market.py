from huobi.utils.http import get
from huobi.host import HOST_FUTURES
import json


class Market:
    def __init__(self, host=HOST_FUTURES):
        self.__host = host

    def get_contract_info(self, params: dict = None) -> json:
        path = "/api/v1/contract_contract_info"
        return get(self.__host, path, params)

    def get_index_info(self, params: dict = None) -> json:
        path = "/api/v1/contract_index"
        return get(self.__host, path, params)

    def get_price_limit(self, params: dict = None) -> json:
        path = "/api/v1/contract_price_limit"
        return get(self.__host, path, params)

    def get_open_interest(self, params: dict = None) -> json:
        path = "/api/v1/contract_open_interest"
        return get(self.__host, path, params)

    def get_delivery_price(self, params: dict = None) -> json:
        path = "/api/v1/contract_delivery_price"
        return get(self.__host, path, params)

    def get_estimated_settlement_price(self, params: dict = None) -> json:
        path = "/api/v1/contract_estimated_settlement_price"
        return get(self.__host, path, params)

    def get_api_state(self, params: dict = None) -> json:
        path = "/api/v1/contract_api_state"
        return get(self.__host, path, params)

    def get_depth(self, params: dict = None) -> json:
        path = "/market/depth"
        return get(self.__host, path, params)

    def get_bbo(self, params: dict = None) -> json:
        path = "/market/bbo"
        return get(self.__host, path, params)

    def get_kline(self, params: dict = None) -> json:
        path = "/market/history/kline"
        return get(self.__host, path, params)

    def get_mark_price_kline(self, params: dict = None) -> json:
        path = "/index/market/history/mark_price_kline"
        return get(self.__host, path, params)

    def get_merged(self, params: dict = None) -> json:
        path = "/market/detail/merged"
        return get(self.__host, path, params)

    def get_batch_merged(self, params: dict = None) -> json:
        path = "/market/detail/batch_merged"
        return get(self.__host, path, params)

    def get_trade(self, params: dict = None) -> json:
        path = "/market/trade"
        return get(self.__host, path, params)

    def get_history_trade(self, params: dict = None) -> json:
        path = "/market/history/trade"
        return get(self.__host, path, params)

    def get_risk_info(self, params: dict = None) -> json:
        path = "/api/v1/contract_risk_info"
        return get(self.__host, path, params)

    def get_insurance_fund(self, params: dict = None) -> json:
        path = "/api/v1/contract_insurance_fund"
        return get(self.__host, path, params)

    def get_adjustfactor(self, params: dict = None) -> json:
        path = "/api/v1/contract_adjustfactor"
        return get(self.__host, path, params)

    def get_his_open_interest(self, params: dict = None) -> json:
        path = "/api/v1/contract_his_open_interest"
        return get(self.__host, path, params)

    def get_ladder_margin(self, params: dict = None) -> json:
        path = "/api/v1/contract_ladder_margin"
        return get(self.__host, path, params)

    def get_elite_account_ratio(self, params: dict = None) -> json:
        path = "/api/v1/contract_elite_account_ratio"
        return get(self.__host, path, params)

    def get_elite_position_ratio(self, params: dict = None) -> json:
        path = "/api/v1/contract_elite_position_ratio"
        return get(self.__host, path, params)

    def get_liquidation_orders(self, params: dict = None) -> json:
        path = "/api/v1/contract_liquidation_orders"
        return get(self.__host, path, params)

    def get_settlement_records(self, params: dict = None) -> json:
        path = "/api/v1/contract_settlement_records"
        return get(self.__host, path, params)

    def get_index_kline(self, params: dict = None) -> json:
        path = "/index/market/history/index"
        return get(self.__host, path, params)

    def get_basis(self, params: dict = None) -> json:
        path = "/index/market/history/basis"
        return get(self.__host, path, params)
