from huobi.utils.ws import Ws
from huobi.host import HOST_SPOT
import json


class Market():
    def __init__(self, host: str = HOST_SPOT):
        self.__host = host
        self.__path = "/ws"
        self.__mbp_path = "/feed"

    def sub(self, data: dict, call_back_fun) -> Ws:
        ws = Ws(self.__host, self.__path, data, call_back_fun)
        ws.connect()
        return ws

    def req(self, data: dict, call_back_fun) -> Ws:
        ws = Ws(self.__host, self.__path, None, call_back_fun)
        ws.connect()
        ws.send_msg(data)
        return 
        
    def sub_mbp(self, data: dict, call_back_fun) -> Ws:
        '''
        just for Market By Price
        '''
        ws = Ws(self.__host, self.__mbp_path, data, call_back_fun)
        ws.connect()
        return ws

    def req_mbp(self, data: dict, call_back_fun) -> Ws:
        '''
        just for Market By Price
        '''
        ws = Ws(self.__host, self.__mbp_path, None, call_back_fun)
        ws.connect()
        ws.send_msg(data)
        return ws
