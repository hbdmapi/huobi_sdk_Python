import websocket
import threading
import gzip
import json
from datetime import datetime
from urllib import parse
import hmac
import base64
from hashlib import sha256
import time

from huobi.utils.logger import logger


class Ws:
    def __init__(self, host: str, path: str, sub_str: dict, call_back_fun,
                 access_key: str = None, secret_key: str = None,
                 auto_reconnect=True):
        self.__host = host
        self.__path = path
        self.__url = 'wss://{}{}'.format(self.__host, self.__path)
        self.__sub_str = sub_str
        self.__call_back_fun = call_back_fun
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__auto_reconnect = auto_reconnect

        self.__ws = None
        self.__be_open = False
        self.__be_active_close = False

    def __del__(self):
        self.close()

    def connect(self):
        if self.__ws is not None:
            return
        self.__ws = websocket.WebSocketApp(self.__url,
                                           on_open=self.__on_open,
                                           on_message=self.__on_msg,
                                           on_close=self.__on_close,
                                           on_error=self.__on_error)
        t = threading.Thread(target=self.__ws.run_forever, daemon=True)
        t.start()

    def close(self):
        if self.__ws is None:
            return
        self.__be_active_close = True
        self.__ws.close()

    def __send_auth_data(self, method: str, host: str, path: str, access_key: str, secret_key: str):
        # timestamp
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

        # get Signature
        suffix = 'AccessKeyId={}&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp={}'.format(
            access_key, parse.quote(timestamp))
        payload = '{}\n{}\n{}\n{}'.format(method.upper(), host, path, suffix)

        digest = hmac.new(secret_key.encode('utf8'), payload.encode(
            'utf8'), digestmod=sha256).digest()
        signature = base64.b64encode(digest).decode()

        # data
        data = {
            "op": "auth",
            "type": "api",
            "AccessKeyId": access_key,
            "SignatureMethod": "HmacSHA256",
            "SignatureVersion": "2",
            "Timestamp": timestamp,
            "Signature": signature
        }
        data = json.dumps(data)
        self.__ws.send(data)
        logger.info('send data: {}'.format(data))

    def __on_open(self, ws):
        self.__be_open = True
        logger.info('ws open: {}'.format(self.__url))
        if self.__access_key is not None or self.__secret_key is not None:
            self.__send_auth_data('get', self.__host, self.__path,
                                  self.__access_key, self.__secret_key)
        else:
            if self.__sub_str is not None:
                data = json.dumps(self.__sub_str)
                self.__ws.send(data)
                logger.info('send data: {}'.format(data))

    def __on_msg(self, ws, message):
        plain = gzip.decompress(message).decode()
        jdata = json.loads(plain)
        if 'ping' in jdata:
            sdata = plain.replace('ping', 'pong')
            self.__ws.send(sdata)
        elif 'op' in jdata:
            opdata = jdata['op']
            if opdata == 'ping':
                sdata = plain.replace('ping', 'pong')
                self.__ws.send(sdata)
            elif opdata == 'auth':
                logger.info(plain)
                if self.__sub_str is not None and jdata['err-code'] == 0:
                    data = json.dumps(self.__sub_str)
                    self.__ws.send(data)
                    logger.info('send data: {}'.format(data))
            elif opdata == 'sub' or opdata == 'unsub' or opdata == 'close':
                logger.info(plain)
            elif opdata == 'notify':
                if self.__call_back_fun is not None:
                    self.__call_back_fun(jdata)
            else:
                logger.error('unknow data: {}'.format(jdata))
        elif 'subbed' in jdata:
            logger.info(plain)
        elif 'ch' in jdata:
            if self.__call_back_fun is not None:
                self.__call_back_fun(jdata)
        elif 'rep' in jdata:
            if self.__call_back_fun is not None:
                self.__call_back_fun(jdata)
        else:
            logger.error('unknow data: {}'.format(jdata))

    def __on_close(self, ws, code, msg):
        self.__be_open = False
        logger.info("ws close: {} as {}".format(self.__url, code))
        if not self.__be_active_close and self.__auto_reconnect:
            self.connect()

    def __on_error(self, ws, error):
        logger.error(error)

    def send_msg(self, msg: dict, time_out_sec: int = 3) -> bool:
        if self.__ws is None:
            return False
        times_try = 0
        while not self.__be_open and times_try < time_out_sec:
            time.sleep(1)
            times_try += 1
        data = json.dumps(msg)
        self.__ws.send(data)
        logger.info('send data: {}'.format(data))
        return True

    def is_open(self) -> bool:
        return self.__be_open
