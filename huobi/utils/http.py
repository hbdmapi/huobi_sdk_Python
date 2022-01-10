from huobi.utils.logger import logger

import requests
from urllib import parse
import json
from datetime import datetime
import hmac
import base64
from hashlib import sha256
import traceback


def get(host: str, path: str, params: dict = None, access_key: str = None, secret_key: str = None) -> json:
    try:
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        if access_key is not None or secret_key is not None:
            url = 'https://{}{}?{}'.format(host, path, get_url_suffix(
                'get', host, path, access_key, secret_key, params))
            res = requests.get(url, headers=headers)
        else:
            url = 'https://{}{}'.format(host, path)
            res = requests.get(url, params=params, headers=headers)
        data = res.json()
        return data
    except Exception:
        logger.error(traceback.format_exc())
    return None


def get_url_suffix(method: str, host: str, path: str, access_key: str, secret_key: str, params: dict = None) -> str:
    if params is None:
        params = {}
    params['AccessKeyId'] = access_key
    params['SignatureMethod'] = 'HmacSHA256'
    params['SignatureVersion'] = '2'

    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    timestamp = parse.quote(timestamp)
    params['Timestamp'] = timestamp

    suffix = ''
    for k in sorted(params.keys()):
        suffix += '&{}={}'.format(k, params[k])
    if suffix != '':
        suffix = suffix[1:]
    payload = '{}\n{}\n{}\n{}'.format(method.upper(), host, path, suffix)

    digest = hmac.new(secret_key.encode('utf8'), payload.encode(
        'utf8'), digestmod=sha256).digest()
    signature = base64.b64encode(digest).decode()

    suffix = '{}&Signature={}'.format(suffix, parse.quote(signature))
    return suffix


def post(host: str, path: str, access_key: str, secret_key: str, data: dict = None) -> json:
    try:
        url = 'https://{}{}?{}'.format(host, path, get_url_suffix(
            'post', host, path, access_key, secret_key))
        headers = {'Accept': 'application/json',
                   'Content-type': 'application/json'}
        res = requests.post(url, json=data, headers=headers)
        data = res.json()
        return data
    except Exception:
        logger.error(traceback.format_exc())
    return None
