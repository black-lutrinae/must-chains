from block import Block
import hashlib as hash


class Blockchain():
    def __init__(self):
        self.blocks = []
        self.difficulty = 0
        self.count = 0

    def verify_block(self, block):
        if not isinstance(block, Block):
            return False
        if block.index != (self.count + 1):
            return False
        if block.prev_hash != self.blocks[len(self.blocks)-1].block_hash:
            return False
        proof, block_hash = block.hash()
        if not block_hash.startswith('0' * (self.difficulty + 1)):
            return False
        return True

    def add_block(self, block):
        if self.verify_block(block):
            self.blocks.append(block)
            self.count = self.count + 1
            self.difficulty = self.difficulty + 1
        else:
            print('Invalid Block!')
    
    def add_genesis(self, block):
        if len(self.blocks) == 0:
            if isinstance(block, Block):
                block.mine()
                self.blocks.append(block)
                self.difficulty = block.difficulty
                self.count = block.index
            else:
                print('Invalid Block!')
        else:
            print('Operation Denied!')