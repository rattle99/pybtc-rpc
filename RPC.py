import requests


class rpc(object):
    """A class wrapping basic remote procedure calls to a locally running bitcoin node.

    Args:
        object (_type_): _description_
    """

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
        """Returns header hash of block in local blockchain at height provided.

        Args:
            number (int): block number

        Returns:
            str: blockhash
        """

        self.payload["method"] = "getblockhash"
        self.payload["params"] = [number]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlock(self, blockHash, verbosity=1):
        """Get blockdata by block header hash.

        Args:
            blockHash (str): block hash
            verbosity (int, optional): 1 for block data without tx data, 2 for block with tx data. Defaults to 1.

        Returns:
            dict: block data
        """

        self.payload["method"] = "getblock"
        self.payload["params"] = [blockHash, verbosity]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockHeader(self, blockHash, verbose=True):
        """Get block header by blockhash

        Args:
            blockHash (str): block hash
            verbose (bool, optional): True for json object, False for hex encoded. Defaults to True.

        Returns:
            _type_: _description_
        """

        self.payload["method"] = "getblockheader"
        self.payload["params"] = [blockHash, verbose]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockStats(self, blockHash):
        """Compute block statistics for a given block

        Args:
            blockHash (str): block hash

        Returns:
            dict: different calculated stats for a given block
        """

        self.payload["method"] = "getblockstats"
        self.payload["params"] = [blockHash]

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockChainInfo(self):
        """Returns an object containing various state info regarding blockchain processing.

        Returns:
            dict: blockchain info
        """

        self.payload["method"] = "getblockchaininfo"
        self.payload["params"] = []

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result

    def getBlockCount(self) -> int:
        """Returns current block count in local chain.

        Returns:
            int: block count
        """

        self.payload["method"] = "getblockcount"
        self.payload["params"] = []

        response = self.session.post(
            self.URL, json=self.payload, headers=self.headers)
        result = response.json()['result']
        return result
