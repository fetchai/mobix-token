#!/usr/bin/python3
from brownie import MobixToken, accounts

totalSupply = 100_000_000_000_000_000

def main():
    foundation = accounts.load('foundation')
    MobixToken.deploy("Wrapped MOBIX", "wMOBX", 9, totalSupply, {'from': foundation}, publish_source=True) 

