from web3 import Web3
def handle_new_block(block):
    transactions = block['transactions']
    for tx in transactions:
        tx_details = web3.eth.get_transaction(tx.hex())
        print("Transaction:", tx_details)

# Subscribe to new blocks
from web3.middleware import geth_poa_middleware
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
new_block_filter = web3.eth.filter('latest')
new_block_filter.watch(handle_new_block)