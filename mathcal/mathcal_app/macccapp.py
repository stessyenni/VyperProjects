from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from web3 import Web3
import os

print("Current Working Directory:", os.getcwd())

app = Flask(__name__)
CORS(app)

# Deployed contract details
contract_address = "0x7b96aF9Bd211cBf6BA5b0dd53aa61Dc5806b6AcE"  # Replace with your contract address
contract_abi = [
    {
        "type": "function",
        "name": "add",
        "stateMutability": "pure",
        "inputs": [{"name": "a", "type": "int128"}, {"name": "b", "type": "int128"}],
        "outputs": [{"name": "", "type": "int128"}],
    },
    {
        "type": "function",
        "name": "divide",
        "stateMutability": "pure",
        "inputs": [{"name": "a", "type": "int128"}, {"name": "b", "type": "int128"}],
        "outputs": [{"name": "", "type": "int128"}],
    },
    {
        "type": "function",
        "name": "multiply",
        "stateMutability": "pure",
        "inputs": [{"name": "a", "type": "int128"}, {"name": "b", "type": "int128"}],
        "outputs": [{"name": "", "type": "int128"}],
    },
    {
        "type": "function",
        "name": "subtract",
        "stateMutability": "pure",
        "inputs": [{"name": "a", "type": "int128"}, {"name": "b", "type": "int128"}],
        "outputs": [{"name": "", "type": "int128"}],
    },
]

# Connect to Ethereum node
infura_url = "ttp://127.0.0.1:7545"  # Replace with your Infura project ID
web3 = Web3(Web3.HTTPProvider(ganaMACche_url))

if web3.isConnected():
    print("Connected to Ganache!")
else:
    raise Exception("Failed to connect to Ganache!")

# Initialize contract
try:
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
except Exception as e:
    raise Exception(f"Error initializing contract: {e}")


@app.route("/")
def index():
    """Serve the main frontend HTML file."""
    return render_template("index.html")


# Helper function for error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


# Arithmetic Operations
@app.route("/add", methods=["POST"])
def add():
    data = request.json
    if not data or "a" not in data or "b" not in data:
        return error_response("Missing parameters 'a' or 'b'")
    try:
        a = int(data["a"])
        b = int(data["b"])
        result = contract.functions.add(a, b).call()
        return jsonify({"result": result})
    except Exception as e:
        return error_response(f"Error processing addition: {e}", 500)


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.json
    if not data or "a" not in data or "b" not in data:
        return error_response("Missing parameters 'a' or 'b'")
    try:
        a = int(data["a"])
        b = int(data["b"])
        result = contract.functions.subtract(a, b).call()
        return jsonify({"result": result})
    except Exception as e:
        return error_response(f"Error processing subtraction: {e}", 500)


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.json
    if not data or "a" not in data or "b" not in data:
        return error_response("Missing parameters 'a' or 'b'")
    try:
        a = int(data["a"])
        b = int(data["b"])
        result = contract.functions.multiply(a, b).call()
        return jsonify({"result": result})
    except Exception as e:
        return error_response(f"Error processing multiplication: {e}", 500)


@app.route("/divide", methods=["POST"])
def divide():
    data = request.json
    if not data or "a" not in data or "b" not in data:
        return error_response("Missing parameters 'a' or 'b'")
    try:
        a = int(data["a"])
        b = int(data["b"])
        result = contract.functions.divide(a, b).call()
        return jsonify({"result": result})
    except Exception as e:
        return error_response(f"Error processing division: {e}", 500)


if __name__ == "__main__":
    app.run(debug=True)
