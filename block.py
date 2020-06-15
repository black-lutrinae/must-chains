import hashlib as hash
import random, time, math

class Block():


    def __init__(self, index, prev_hash, data, difficulty=1):
        self.prev_hash = prev_hash
        self.difficulty = difficulty
        self.index = index
        self.data = data
        self.nonce = 0
        self.proof = None

    def hash(self):
        data = "".join(self.data)
        index = str(self.index)
        prev = str(self.prev_hash)
        if self.proof:
            salt = self.proof
        else:
            if self.nonce - math.ceil(self.nonce) != 0:
                salt = str(random.randint(math.floor(self.nonce), math.ceil(self.nonce) ** self.difficulty))
            else:
                salt = str(int(self.nonce))
        block = data + salt + index + prev
        return salt, hash.sha256(block.encode()).hexdigest()


    def mine(self):
        passed = False
        start = time.time()
        while not passed:
            self.nonce = self.nonce + 0.5
            proof, attempt = self.hash()
            if attempt.startswith('0' * self.difficulty):
                print(str(time.time() - start)+'s')
                passed = True
                block_hash = attempt
        self.block_hash = block_hash
        self.proof = proof
