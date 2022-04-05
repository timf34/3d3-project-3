import socket
from flask import Flask , request
import requests
import json
import time
from typing import Tuple, Union

from blockchain import Blockchain
from block import Block


app = Flask(__name__)

blockchain = Blockchain()
blockchain.create_genesis_block()

peers = set()


def consensus() -> bool:
    """
    Our consensus algorithm, which resolves conflicts by replacing our chain with the longest one in the network.
    :return: <bool> True if our chain was replaced, False if not

    Modified version from https://github.com/satwikkansal/python_blockchain_app/blob/master/node_server.py
    """
    global blockchain
    longest_chain = None
    current_len = len(blockchain.chain)

    for node in peers:
        response = requests.get('http://{}/chain'.format(node)) # TODO: check if this works, it differs from the original
        length = response.json()['length']
        chain = response.json()['chain']

        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False


def announce_new_block(block) -> None:
    """
    A function to announce to the network once a block has been mined.
    Other blocks can simply verify the proof of work and add it to their
    respective chains.
    """
    # TODO: again check this - it differs from the original
    for peer in peers:
        url = "http://{}/add_block".format(peer)
        requests.post(url, data=json.dumps(block.__dict__, sort_keys=True))


@app.route('/new_transaction', methods=['POST'])
def new_transaction() -> Tuple[str, int]:
    """
    Creates a new transaction to go into the next mined Block
    :return:

    modified from the GitHub mentioned above
    """
    tx_data = request.get_json()
    required_fields = ["author", "content"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 404

    tx_data["timestamp"] = time.time()
    blockchain.add_new_transaction(tx_data)

    return "Success", 201


@app.route('/chain', methods=['GET'])
def get_chain():
    """
    A GET request to the node.
    :return: <str> A json representation of the node's chain.
    """
    chain_data = [block.__dict__ for block in blockchain.chain]
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "peers": list(peers)})


@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    """
    Mines all unconfirmed transactions, and adds a new block to the chain.
    :return: <str> The added block.
    """
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    chain_length = len(blockchain.chain)
    consensus()
    if chain_length == len(blockchain.chain):
        # announce the recently mined block to the network
        announce_new_block(blockchain.last_block)
    return f"Block #{blockchain.last_block.index} is mined."


@app.route('/register_node', methods=['POST'])
def register_new_peers() -> Union[Tuple[str, int], bool]:
    """
    Registers a new peer in the network.
    :return: <str> The added block.
    """
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    # Add the node to the peer list
    peers.add(node_address)

    return consensus()


@app.route('/register_with', methods=['POST'])
def register_with_existing_node() -> Union[Tuple[str, int], bool]:
    """
    Registers a new peer in the network.
    :return: <str> The added block.
    """
    # TODO: test this function, it might be very short
    #  Yes this will most likely need to be changed
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    # Add the node to the peer list
    peers.add(node_address)

    # Get the chain from the node.
    response = requests.get(f'http://{node_address}/chain')

    if response.status_code != 200:
        return False
    length = response.json()['length']
    chain = response.json()['chain']
    # Check if the length is longer and the chain is valid.
    if length > len(blockchain.chain) and blockchain.is_valid_chain(chain):
        blockchain.chain = chain
    return consensus()


def create_chain_from_dump(dump):
    """
    Creates a chain from a dump
    :param dump:
    :return:
    """
    # TODO: test this function too
    generated_blockchain = Blockchain()
    generated_blockchain.create_genesis_block()
    for idx, block_data in enumerate(dump):
        if idx == 0:
            continue  # skip genesis block
        block = Block(block_data["index"],
                      block_data["transactions"],
                      block_data["timestamp"],
                      block_data["previous_hash"])
        proof = block_data['hash']
        added = generated_blockchain.add_block(block, proof)
        if not added:
            raise Exception("The chain dump is tampered!!")
    return generated_blockchain


@app.route('/add_block', methods=['POST'])
def verify_and_add_block():
    """
    Adds a block to the chain.
    :return: <str> The added block.
    """
    block_data = request.get_json()
    block = Block(block_data["index"],
                  block_data["transactions"],
                  block_data["timestamp"],
                  block_data["previous_hash"])

    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "The block was discarded by the node", 400

    return "Block added to the chain", 201


def get_pending_transactions():
    """
    Returns the pending transactions
    :return: <list>
    """
    transactions = blockchain.current_transactions
    return json.dumps(dict(pending_transactions=transactions))


def test_app():
    """
    Tests the app.
    :return:
    """
    app.run(debug=True, port=5000)


if __name__ == '__main__':
    test_app()




