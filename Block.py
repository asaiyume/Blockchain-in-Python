import hashlib
import datetime
from Blockchain import blockchain


class Block:
    def __init__(self, index, previousBlockHash, data, timestamp):
        self.index = index
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
        return Block(0, 0, 0, datetime.datetime.now())

    def createBlock(self, blockchain):
        currentindex = len(blockchain)
        previoushash = blockchain[-1].hash()
        data = input("Enter your data: ")
        timestamp = datetime.datetime.now()
        newblock = Block(currentindex, previoushash, data, timestamp)
        blockchain.append(newblock)
        return blockchain
