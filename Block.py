import hashlib
import datetime


class Block:
    def __init__(self, previousBlockHash, data, timestamp):
        self.previousBlockHash = previousBlockHash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.getHash()

    def getHash(self):
        header = (str(self.previousBlockHash) +
                  str(self.data) + str(self.timestamp)).encode()
        digest = hashlib.sha256(header).hexdigest()
        return digest

    @staticmethod
    def createGenesisBlock():
        return Block(0, 0, datetime.datetime.now())
