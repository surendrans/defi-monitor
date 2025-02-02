from web3 import Web3
from config import INFURA_URL

class MonitoringAgent:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    def run(self):
        if self.web3.isConnected():
            print("Monitoring agent started")
            # Add your monitoring logic here
        else:
            print("Failed to connect to Ethereum network")

# Example usage
if __name__ == "__main__":
    agent = MonitoringAgent()
    agent.run()