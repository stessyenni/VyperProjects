from brownie import accounts, mathcal

def main():
    account = accounts[0]
    mathcal_contract = mathcal.load('/').mathcal.deploy({'from': account})
    print("Contract deployed at:", mathcal_contract.address)
