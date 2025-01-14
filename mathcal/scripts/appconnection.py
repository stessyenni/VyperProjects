from web3 import Web3

# Connect to Ethereum node
infura_url = "https://sepolia.infura.io/v3/ff8138aeaf2045cabfc9b82761282017"  # Replace with your Infura project ID
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected():
    print("Connected to Ethereum!")
else:
    raise Exception("Failed to connect to Ethereum!")

# Initialize contract
try:
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
except Exception as e:
    raise Exception(f"Error initializing contract: {e}")
