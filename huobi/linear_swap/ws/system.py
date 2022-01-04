from huobi.utils.ws import Ws
from huobi.host import HOST_FUTURES


class System(Ws):
    def __init__(self, host: str = HOST_FUTURES):
        self.__host = host
        self.__path = "/center-notification"

    def sub(self, data: dict, call_back_fun) -> Ws:
        ws = Ws(self.__host, self.__path, data, call_back_fun)
        ws.connect()
        return ws
