from huobi.utils.http import get
from huobi.host import HOST_FUTURES
import json


class Market:
    def __init__(self, host=HOST_FUTURES):
        self.__host = host

    def get_contract_info(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_contract_info"
        return get(self.__host, path, params)

    def get_index_info(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_index"
        return get(self.__host, path, params)

    def get_price_limit(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_price_limit"
        return get(self.__host, path, params)

    def get_open_interest(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_open_interest"
        return get(self.__host, path, params)

    def get_depth(self, params: dict = None) -> json:
        path = "/swap-ex/market/depth"
        return get(self.__host, path, params)

    def get_bbo(self, params: dict = None) -> json:
        path = "/swap-ex/market/bbo"
        return get(self.__host, path, params)

    def get_kline(self, params: dict = None) -> json:
        path = "/swap-ex/market/history/kline"
        return get(self.__host, path, params)

    def get_mark_price_kline(self, params: dict = None) -> json:
        path = "/index/market/history/swap_mark_price_kline"
        return get(self.__host, path, params)

    def get_merged(self, params: dict = None) -> json:
        path = "/swap-ex/market/detail/merged"
        return get(self.__host, path, params)

    def get_batch_merged(self, params: dict = None) -> json:
        path = "/swap-ex/market/detail/batch_merged"
        return get(self.__host, path, params)

    def get_trade(self, params: dict = None) -> json:
        path = "/swap-ex/market/trade"
        return get(self.__host, path, params)

    def get_history_trade(self, params: dict = None) -> json:
        path = "/swap-ex/market/history/trade"
        return get(self.__host, path, params)

    def get_risk_info(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_risk_info"
        return get(self.__host, path, params)

    def get_insurance_fund(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_insurance_fund"
        return get(self.__host, path, params)

    def get_adjustfactor(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_adjustfactor"
        return get(self.__host, path, params)

    def get_his_open_interest(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_his_open_interest"
        return get(self.__host, path, params)

    def get_ladder_margin(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_ladder_margin"
        return get(self.__host, path, params)

    def get_elite_account_ratio(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_elite_account_ratio"
        return get(self.__host, path, params)

    def get_elite_position_ratio(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_elite_position_ratio"
        return get(self.__host, path, params)

    def get_estimated_settlement_price(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_estimated_settlement_price"
        return get(self.__host, path, params)

    def get_api_state(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_api_state"
        return get(self.__host, path, params)

    def get_funding_rate(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_funding_rate"
        return get(self.__host, path, params)

    def get_batch_funding_rate(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_batch_funding_rate"
        return get(self.__host, path, params)

    def get_historical_funding_rate(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_historical_funding_rate"
        return get(self.__host, path, params)

    def get_liquidation_orders(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_liquidation_orders"
        return get(self.__host, path, params)

    def get_settlement_records(self, params: dict = None) -> json:
        path = "/swap-api/v1/swap_settlement_records"
        return get(self.__host, path, params)

    def get_premium_index_kline(self, params: dict = None) -> json:
        path = "/index/market/history/swap_premium_index_kline"
        return get(self.__host, path, params)

    def get_estimated_rate_kline(self, params: dict = None) -> json:
        path = "/index/market/history/swap_estimated_rate_kline"
        return get(self.__host, path, params)

    def get_basis(self, params: dict = None) -> json:
        path = "/index/market/history/swap_basis"
        return get(self.__host, path, params)
