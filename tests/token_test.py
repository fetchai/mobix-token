#!/usr/bin/python3

import pytest
import brownie
from brownie import MobixToken

totalSupply = 100_000_000_000_000_000
amount = 1000

@pytest.fixture(scope="module", autouse=True)
def token(MobixToken, accounts):
    yield MobixToken.deploy("MOBIX", "MOBX", 9, totalSupply, {'from': accounts[0]})

@pytest.fixture(autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

def test_initiation(token, accounts):
    assert token.totalSupply() == totalSupply
    assert token.name() == "MOBIX"
    assert token.decimals() == 9 
    assert token.symbol() == "MOBX"

def test_transfer(token, accounts):
    assert token.transfer(accounts[1], amount, {'from': accounts[0]}).return_value
    assert token.balanceOf(accounts[1]) == amount
    assert token.balanceOf(accounts[0]) == totalSupply - amount

def test_transfer_fail(token, accounts):
    with brownie.reverts():
        token.transfer(accounts[0], amount, {'from': accounts[1]})

def test_approve(token, accounts):
    assert token.approve(accounts[1], amount, {'from': accounts[0]}).return_value
    assert token.allowance(accounts[0], accounts[1]) == amount
    with brownie.reverts():
        token.transferFrom(accounts[0], accounts[2], amount+1, {'from': accounts[1]})
    assert token.transferFrom(accounts[0], accounts[2], amount, {'from': accounts[1]}).return_value

def test_change_allowance(token, accounts):
    with brownie.reverts():
        token.decreaseAllowance(accounts[1], amount, {'from': accounts[0]})

    assert token.increaseAllowance(accounts[1], amount, {'from': accounts[0]}).return_value
    assert token.allowance(accounts[0], accounts[1]) == amount
    assert token.decreaseAllowance(accounts[1], 1, {'from': accounts[0]}).return_value 
    assert token.allowance(accounts[0], accounts[1]) == amount-1

def test_approve_revoke(token, accounts):
    assert token.approve(accounts[1], amount, {'from': accounts[0]}).return_value
    assert token.approve(accounts[1], 0, {'from': accounts[0]}).return_value
    assert token.allowance(accounts[0], accounts[1]) == 0
    with brownie.reverts():
        token.transferFrom(accounts[0], accounts[2], 1, {'from': accounts[1]})
