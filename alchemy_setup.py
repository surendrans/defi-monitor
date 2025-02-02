from web3 import Web3

# Connect to Ethereum node
infura_url = "https://eth-sepolia.g.alchemy.com/v2/GmNy3euhlFiol4XgBUGMJXS-yuOD-iHL"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect")

# Fetch the latest block
latest_block = web3.eth.get_block('latest')
print("Latest block:", latest_block)

# Function to handle new blocks
def handle_new_block(block):
    print("New block:", block['number'])

# Subscribe to new blocks
new_block_filter = web3.eth.filter('latest')
new_block_filter.watch(handle_new_block)

def is_suspicious(tx):
    # High-value transactions
    if web3.fromWei(tx['value'], 'ether') > 100:  # 100 ETH
        return True
    # Unusual gas fees
    if tx['gasPrice'] > web3.toWei('200', 'gwei'):
        return True
    # Known scam addresses (example)
    scam_addresses = ["0xScamAddress1", "0xScamAddress2"]
    if tx['to'] in scam_addresses:
        return True
    return False

from sklearn.ensemble import IsolationForest

# Example features: value, gas price, gas used, etc.
def extract_features(tx):
    return [web3.fromWei(tx['value'], 'ether'), tx['gasPrice'], tx['gas']]

# Train an Isolation Forest model (example)
transactions = [...]  # List of historical transactions
X = [extract_features(tx) for tx in transactions]
model = IsolationForest(contamination=0.1)
model.fit(X)

# Predict if a transaction is suspicious
def is_suspicious_ai(tx):
    features = extract_features(tx)
    return model.predict([features])[0] == -1


class MonitoringAgent:
    def __init__(self):
        self.new_block_filter = web3.eth.filter('latest')

    def run(self):
        self.new_block_filter.watch(self.handle_new_block)

    def handle_new_block(self, block):
        transactions = block['transactions']
        for tx in transactions:
            tx_details = web3.eth.get_transaction(tx.hex())
            if is_suspicious(tx_details) or is_suspicious_ai(tx_details):
                print("Suspicious transaction detected:", tx_details)

# Start the agent
monitoring_agent = MonitoringAgent()
monitoring_agent.run()