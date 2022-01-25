from huobi.utils.http import get, post
from huobi.host import HOST_SPOT
import json


class StableCoin:
    def __init__(self, access_key: str, secret_key: str, host=HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def get_quote(self, params: dict) -> json:
        path = "/v1/stable-coin/quote"
        return get(self.__host, path, params)

    def exchange(self, params: dict) -> json:
        path = "/v1/stable-coin/exchang"
        return post(self.__host, path, self.__access_key, self.__secret_key, params)
