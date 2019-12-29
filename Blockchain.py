import Block
import hashlib
import datetime

blockchain = [Block.Block.createGenesisBlock()]


def createBlock(blockchain):
    currentindex = len(blockchain)
    previoushash = blockchain[-1].hash
    data = input("Enter your data: ")
    timestamp = datetime.datetime.now()
    newblock = Block.Block(currentindex, previoushash, data, timestamp)
    return newblock


while True:
    userinput = input(
        "Welcome to Blockchain!\n[1] View Blockchain\n[2] Generate new block & add to blockchain\n[3] Exit\nChoose the action you want to do: ")
    if int(userinput) == 1:
        for i in blockchain:
            print("Index: {}\nHash: {}\nPrevious Hash: {}\nData: {}\nTimestamp: {}\n{}".format(
                i.index, i.hash, i.previousBlockHash, i.data, i.timestamp, "="*70))
    elif int(userinput) == 2:
        block = createBlock(blockchain)
        blockchain.append(block)
        print("A new block has been added!\nIndex: {}\nHash: {}\nPrevious Hash: {}\nData: {}\nTimestamp: {}".format(
            block.index, block.hash, block.previousBlockHash, block.data, block.timestamp))
    elif int(userinput) == 3:
        exit()
