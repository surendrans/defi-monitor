import streamlit as st
from web3 import Web3
from config import INFURA_URL

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

st.title("DeFi Transaction Monitor")

if web3.isConnected():
    st.write("Connected to Ethereum network")
else:
    st.write("Failed to connect")

# Add your dashboard logic here