# Huobi Python SDK

This is Huobi Python SDK, requires python >= 3.6.

The SDK API supports both RESTful and websocket to get/sub the market, account and order infomation.

It supports Spot trading, Coin-M Futures, Coin-M Swaps and USDT-M.

You can install this package with `pip3 install huobipy`

## Table of Contents

- [Quick Start](#Quick-Start)

- [Usage](#Usage)

  - [Configuration](#Configuration)
  - [Folder structure](#Folder-Structure)
  - [Client](#Client)
  - [Request](#Request)
  - [Response](#Response)

## Quick Start

The project **huobi** is a dll project as SDK API.
The project **tests** is a unit test project and you can find usage of each API interface.

If you want to create your own application, you can follow below steps:

* Create a client instance.
* Call the method of client instance.

```python
// RESTful 
from huobi.linear_swap.rest.account import Account
client = Account(ACCESS_KEY, SECRET_KEY)
result = client.get_balance_valuation({"valuation_asset": "usdt"})

// websocket
from huobi.linear_swap.ws.account import Account
client = Account(ACCESS_KEY, SECRET_KEY)
client.sub({"op": "sub", "topic": "orders.btc-usdt"},
            lambda x: logger.info(x))
time.sleep(10)
```

## Usage

### Configuration

The client constructor must set AccessKey/SecretKey two value when you access private data. And it not need to set AccessKey/SecretKey value when you access public data such as market data.

You can create config.py in your project for config AccessKey/SecretKey and other input data.

```python
ACCESS_KEY = "x-x-x-x"
SECRET_KEY = "x-x-x-x"
```

And use it as follow:
```python
from config import ACCESS_KEY, SECRET_KEY
# to do something
 ```

### Folder Structure

This is the folder and namespace structure of SDK source code and the description

- **huobi**: The SDK API project
  - **spot**: the Spot trading api src inclue RESTful and Websocket
  - **futures**: the Coin-M Futures api src inclue RESTful and Websocket
  - **coin_swap**: the Coin-M Swaps api src inclue RESTful and Websocket
  - **linear_swap**: the USDT-M api src inclue RESTful and Websocket
  - **utils**: http.get/post lib, websocket api lib and log setting
  - **host.py**: the host name of spot and futures(Coin-M Futures, Coin-M Swaps and USDT-M are using the same host name)
- **tests**: The unit test project
  - **config.py**: config of accessKey and secretKey
  - **xxx**: The Python unit test folder

You can find all demo in test_xxx.py to get/sub private/public data

### Client

In this SDK, the client is the object to access the Huobi API. All the client are listed in below table. Each client is very small and simple.

| Access Type | Client | Privacy | Data Category  |
| ----------- | -------| ------- | ------------ |
| RESTful     | Account | Private | account info |
|             | Market | Public | market info |
|             | Order | Private | about order |
|             | Transfer | Private | transfer assets |
|             | TriggerOrder | Private | about trigger order |
| Websocket   | Index | Public | index infor |
|             | Market | Public | market info |
|             | Notify | Public/Private | market info/ account info |
|             |                |         |              |

#### Public vs. Private

There are two types of privacy that is correspondent with privacy of API:

**Public client**: It invokes public API to get public data (Common data and Market data), therefore you can create a new instance without applying an API Key.

```python
from huobi.linear_swap.rest.market import Market
client = Market()
result = client.get_contract_info({"contract_code": "btc-usdt", "support_margin_mode": "all"})
```

**Private client**: It invokes private API to access private data, you need to follow the API document to apply an API Key first, and pass the API Key to the constructor.

```python
from huobi.linear_swap.rest.account import Account
client = Account(ACCESS_KEY, SECRET_KEY)
result = client.get_balance_valuation({"valuation_asset": "usdt"})
```

The API key is used for authentication. If the authentication cannot pass, the invoking of private interface will fail.

#### Rest vs. WebSocket

**Rest Client**: It invokes Rest API and get once-off response.

```python
from huobi.linear_swap.rest.account import Account
client = Account(ACCESS_KEY, SECRET_KEY)
result = client.get_balance_valuation({"valuation_asset": "usdt"})
```

**WebSocket Client**: It establishes WebSocket connection with server and data will be pushed from server actively. There are two types of method for WebSocket client:

- Request method: The method name starts with "req", it will receive the once-off data after sending the request.
- Subscription: The method name starts with "sub", it will receive update after sending the subscription.

```python
from huobi.linear_swap.ws.market import Market
client = Market()
client.sub({"sub": "market.BTC-USDT.kline.1min"}, lambda x: logger.info(x))
while True:
    time.sleep(1)
```

#### Custom host

Each client constructor support an optional host parameter, by default it is in host.py file. If you need to use different host, you can specify the custom host. 

```python
from huobi.linear_swap.rest.account import Account
client = Account(ACCESS_KEY, SECRET_KEY, "your_host")

# to do something
```

### Request

In this SDK, the response is the dict type or None. More detail to see: https://docs.huobigroup.com/docs/spot/v1/en/

### Response

In this SDK, the response is the json data. More detail to see: https://docs.huobigroup.com/docs/spot/v1/en/