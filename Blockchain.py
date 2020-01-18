import Block
import hashlib
import datetime

global blockchain
fileheader = ['Index', 'Hash', 'Previous Hash', 'Data', 'Timestamp\n']
viewer = []
temp = []


def initialize():
        # Create ledger
    try:
        f = open(
            'ledger.csv', 'r+')  # Check if ledger exist
    except FileNotFoundError:
        f = open(
            'ledger.csv', 'w+')  # Creates ledger if ledger does not exist
    if len(f.readlines()) == 0:  # Check if ledger is empty
        f = open(
            'ledger.csv', 'w+')
        for i in range(len(fileheader)-1):
            f.write(fileheader[i]+',')
        f.write(fileheader[-1])  # Add headers
        blockchain = [Block.Block.createGenesisBlock()]
        for blocks in blockchain:  # Add block info
            f.write(str(blocks.index)+','+blocks.hash+',' +
                    blocks.previousBlockHash+','+blocks.data+','+str(blocks.timestamp)+'\n')
        print('Ledger not found, creating new ledger...')
        print('Writing new ledger completed!')
        return blockchain
    else:
        blockchain = []
        f = open(
            'ledger.csv', 'r+')
        for lines in f.readlines():
            lines = lines.strip('\n')
            lines = lines.split(',')
            temp.append(lines)
        for blocks in range(len(temp)-1):
            block = Block.Block(
                temp[blocks+1][0], temp[blocks+1][2], temp[blocks+1][3], temp[blocks+1][4])
            blockchain.append(block)
        return blockchain


def createBlock(blockchain):
    currentindex = len(blockchain)
    print(blockchain)
    print(currentindex)
    previoushash = blockchain[-1].hash
    data = input("Enter your data: ")
    timestamp = datetime.datetime.now()
    newblock = Block.Block(currentindex, previoushash, data, timestamp)
    return newblock


def editledger(blockchain):
    # Create ledger
    f = open(
        'ledger.csv', 'a+')  # Add block info
    f.write(str(blockchain[-1].index)+','+blockchain[-1].hash+',' +
            blockchain[-1].previousBlockHash+','+blockchain[-1].data+','+str(blockchain[-1].timestamp)+'\n')
    print('Ledger is now updated!')
    f.close()
    return blockchain


def viewledger():
    f = open(
        'ledger.csv', 'r+')
    for lines in f.readlines():
        lines = lines.strip('\n')
        lines = lines.split(',')
        viewer.append(lines)
    for outer in range(len(viewer)-1):
        print("Index: {}\nHash: {}\nPrevious Hash: {}\nData: {}\nTimestamp: {}\n{}".format(
            viewer[outer+1][0], viewer[outer+1][1], viewer[outer+1][2], viewer[outer+1][3], viewer[outer+1][4], "="*70))


blockchain = initialize()
while True:
    userinput = input(
        "Welcome to Blockchain!\n[1] View ledger\n[2] Generate new block & add to blockchain\n[3] Exit\nChoose the action you want to do: ")
    if int(userinput) == 1:
        viewledger()
    elif int(userinput) == 2:
        block = createBlock(blockchain)
        blockchain.append(block)
        print("A new block has been added!\nIndex: {}\nHash: {}\nPrevious Hash: {}\nData: {}\nTimestamp: {}".format(
            block.index, block.hash, block.previousBlockHash, block.data, block.timestamp))
        editledger(blockchain)
    elif int(userinput) == 3:
        exit()
