from huobi.utils.ws import Ws
from huobi.host import HOST_FUTURES
import json


class Account():
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_FUTURES):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host
        self.__path = "/notification"
        self.__sub_dict = {}

    def sub(self, data: dict, call_back_fun) -> Ws:
        id = data['topic']
        ws = Ws(self.__host, self.__path, data, call_back_fun, self.__access_key, self.__secret_key)
        ws.connect()
        self.__sub_dict[id] = ws
        return ws

    def unsub(self, data: dict) -> Ws:
        id = data['topic']
        if id not in self.__sub_dict:
            return None
        ws = self.__sub_dict[id]
        ws.send_msg(data)
        return ws
