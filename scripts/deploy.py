from brownie import hetToken
from scripts.helpful_scripts import get_account
from web3 import Web3


initial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    het_token = hetToken.deploy(initial_supply, {"from": account})
    print(f"Token {het_token.name()} deployed!")


def main():
    deploy_token()
