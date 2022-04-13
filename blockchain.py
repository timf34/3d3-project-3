from block import Block
import time

class Blockchain:
    def __init__(self, difficulty: int = 2):
        self.chain = []
        self.unconfirmed_transactions = []
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Creates the genesis block
        """
        genesis_block = Block(0, [], 0, "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Block:
        """
        Returns the last block of the chain
        """
        return self.chain[-1]

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Adds a block to the chain
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def proof_of_work(self, block: Block) -> str:
        """
        Finds a valid proof of work for the block
        """
        """ Note: This doesn't work and was the source of the weird hashes and previous hashes - come back and have
        another look at it!
        proof = 0
        # TODO: I might be missing the .compute_hash() method here instead of relying on the above
        while not self.is_valid_proof(block, proof):
            proof += 1
        return proof
        """
        block.nonce=0
        temp_hash=block.compute_hash()
        while not temp_hash.startswith('0' * self.difficulty):
            block.nonce+=1
            temp_hash=block.compute_hash()

        return temp_hash

    def add_new_transaction(self, transaction: dict) -> None:
        """
        Adds a new transaction to the list of transactions
        """
        self.unconfirmed_transactions.append(transaction)

    def is_valid_proof(self, block, block_hash) -> bool:
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * self.difficulty) and
                block_hash == block.compute_hash())

    def is_valid_chain(cls, chain: list) -> bool:
        """
        Validates the chain
        """
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print("block,", block, "block hash", block.hash)
            if block.previous_hash != last_block.hash:
                return False
            if not cls.is_valid_proof(block, block.hash):
                return False
            last_block = block
            current_index += 1
        return True

    def mine(self) -> bool:
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return True

    def __repr__(self):
        return f'{self.chain}'

    def __len__(self):
        return len(self.chain)


def test():
    blockchain = Blockchain()
    blockchain.create_genesis_block()
    print("blockchain:", blockchain)
    print(len(blockchain))
    print("Beginning mining...")
    for i in range(10):
        blockchain.add_new_transaction(f'Transaction {i}')
        if blockchain.mine():
            print(f"Block {i} mined!")
    print(blockchain)
    print(len(blockchain))

    assert blockchain.is_valid_chain(blockchain.chain), "The chain is not valid"
    assert len(blockchain) == 11, "The chain is not the correct length"


if __name__ == "__main__":
    test()
    # TODO: do a diff between this version and the lastest one - I changed something that messed stuff up







