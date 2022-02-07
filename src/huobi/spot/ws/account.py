from huobi.utils.ws import Ws
from huobi.host import HOST_SPOT
import json


class Account():
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_SPOT):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host
        self.__path = "/ws/v2"
        self.__sub_dict = {}

    def sub(self, data: dict, call_back_fun) -> Ws:
        id = data['ch']
        ws = Ws(self.__host, self.__path, data, call_back_fun, self.__access_key, self.__secret_key, be_spot_account=True)
        ws.connect()
        self.__sub_dict[id] = ws
        return ws

    def unsub(self, data: dict) -> Ws:
        id = data['ch']
        if id not in self.__sub_dict:
            return None
        ws = self.__sub_dict[id]
        ws.send_msg(data)
        return ws
