# app.py
from flask import Flask, request, jsonify
from transaction_monitor import monitor_transactions
import threading

app = Flask(__name__)

@app.route("/start_monitor", methods=["POST"])
def start_monitor():
    """
    Start the transaction monitor.
    """
    threading.Thread(target=monitor_transactions).start()
    return jsonify({"status": "Monitor started"})

if __name__ == "__main__":
    app.run(debug=True)



from web3 import Web3
from config import INFURA_URL

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect")