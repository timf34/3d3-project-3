import hashlib
import time  # for timestamp


class Block(object):
    def __init__(self, index: int, transactions: list, previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = time.time()

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = f'{self.index} {self.transactions} {self.timestamp} {self.previous_hash} {self.nonce}'.encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f'Block: {self.index}\n' \
               f'Transactions: {self.transactions}\n' \
               f'Timestamp: {self.timestamp}\n' \
               f'Previous Hash: {self.previous_hash}\n' \
               f'Hash: {self.compute_hash()}\n'


def test():
    block = Block(0, [], 1564252800, '0')
    print(block)
    print(block.compute_hash())


if __name__ == '__main__':
    test()
    print('Done')
