import requests


class rpc(object):
    def __init__(self, username="user", password="pass", port=8332) -> None:

        self.RPC_USERNAME = username
        self.RPC_PASSWORD = password
        self.RPC_PORT = port
        self.URL = f'http://{self.RPC_USERNAME}:{self.RPC_PASSWORD}@127.0.0.1:{self.RPC_PORT}'
        self.session = requests.Session()
        self.headers = {'content-type': 'application/json'}
        self.payload = {"jsonrpc": "2.0",
                        "method": "",
                        "params": "",
                        "id": "curltext"}

    def getBlockHash(self, number):
        self.payload["method"] = "getblockhash"
        self.payload["params"] = [number]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlock(self, blockHash, verbosity=1):
        self.payload["method"] = "getblock"
        self.payload["params"] = [blockHash, verbosity]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockHeader(self, blockHash, verbose=True):
        self.payload["method"] = "getblockheader"
        self.payload["params"] = [blockHash, verbose]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockStats(self, blockHash):
        self.payload["method"] = "getblockstats"
        self.payload["params"] = [blockHash]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result
