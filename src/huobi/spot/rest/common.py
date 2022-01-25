from huobi.utils.http import get
from huobi.host import HOST_SPOT
import json


class Common:
    def __init__(self, host=HOST_SPOT):
        self.__host = host
        self.__symmary = 'status.huobigroup.com'

    def get_system_status(self) -> json:
        path = "/api/v2/summary.json"
        return get(self.__host, path)

    def get_market_status(self) -> json:
        path = "/v2/market-status"
        return get(self.__host, path)

    def get_symbols(self) -> json:
        path = "/v1/common/symbols"
        return get(self.__host, path)

    def get_currencys(self) -> json:
        path = "/v1/common/currencys"
        return get(self.__host, path)

    def get_chains(self, params: dict = None) -> json:
        path = "/v2/reference/currencies"
        return get(self.__host, path, params)

    def get_system_time(self) -> json:
        path = "/v1/common/timestamp"
        return get(self.__host, path)