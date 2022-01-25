from huobi.utils.ws import Ws
from huobi.host import HOST_FUTURES
import json


class Market():
    def __init__(self, host: str = HOST_FUTURES):
        self.__host = host
        self.__path = "/ws"

    def sub(self, data: dict, call_back_fun) -> Ws:
        ws = Ws(self.__host, self.__path, data, call_back_fun)
        ws.connect()
        return ws

    def req(self, data: dict, call_back_fun) -> Ws:
        ws = Ws(self.__host, self.__path, None, call_back_fun)
        ws.connect()
        ws.send_msg(data)
        return ws
