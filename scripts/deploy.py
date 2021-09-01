from brownie import accounts, Lottery

def main():
    acc = accounts.load('0')
    Lottery.deploy({'from': acc}) 

