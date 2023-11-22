import hashlib
import time
import json

class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 4
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(), 'Genesis'))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        # nBlock.hash = nBlock.calHash()
        nBlock.hash = nBlock.mine(self.difficulty)
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def isValid(self):
        i = 1
        while(i < len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):
                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):
                return False
            i += 1
        return True


class Block():
    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = 0
        self.nonce = 0
        self.hash = self.calHash()

    def calHash(self):
        return hashlib.sha256(str(self.index).encode() +
        str(self.data).encode() +
        str(self.nonce).encode() +
        str(self.timestamp).encode() +
        str(self.previousHash).encode()).hexdigest()

    def mine(self, difficulty):
        ans = ["0"]*difficulty
        answer = "".join(ans)
        while(str(self.hash)[:difficulty] != answer):
            self.nonce += 1
            self.hash = self.calHash()

        print('mined block:', self.hash)
        return self.hash


mybc = BlockChain()
print('\nGenesis block ...')
print(json.dumps(vars(mybc.chain[0]), indent=4))
print("\n")

start_time = time.time();
mybc.addBlock(Block(len(mybc.chain), time.time(), {"amount": 4}))
print('1th Block minig time =', time.time() - start_time)
print("\n")

start_time = time.time();
mybc.addBlock(Block(len(mybc.chain), time.time(), {"amount": 100}))
print('2th Block minig time =', time.time() - start_time)
print("\n")

start_time = time.time();
mybc.addBlock(Block(len(mybc.chain), time.time(), {"amount": 1000}))
print('3th Block minig time =', time.time() - start_time)

print("\n")
print("**************************************************************************************")

i = 0
for block in mybc.chain:
    print("\nblock # [", i, "] =", json.dumps(vars(block), indent=4))
    i += 1
