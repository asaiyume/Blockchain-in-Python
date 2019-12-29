import hashlib
import datetime


class Block:
    def __init__(self, previousBlockHash, data, timestamp):
        self.previousBlockHash = previousBlockHash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.getHash()
