from huobi.utils.http import post
from huobi.host import HOST_SPOT
import json


class Transfer:
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def transfer(self, data: dict = None) -> json:
        path = "/v2/account/transfer"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
