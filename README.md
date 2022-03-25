# Mobix ERC-20 contract

Standard ERC-20 without any functions beyond the standard interface.

Uses eth-brownie python library for deploying and testing contracts. We recommend using `pipenv install` for installing local environment. 

Then create a `.env` file with environment variables for [Infura](https://infura.io/) and [Etherscan](https://etherscan.io/login) API keys. 

```bash
export WEB3_INFURA_PROJECT_ID=1234abdef
export ETHERSCAN_TOKEN=1234ABCDEf

```


Set-up requires installation of latest Openzeppelin contract libary with: 

`brownie pm install OpenZeppelin/openzeppelin-contracts@4.4.1`

Standard brownie `compile` and `test` functions can be used to build and test contracts. 

For deployment:

`brownie run scripts/deploy_token.py`

(Can choose test Kovan deployment by adding `--network kovan`)

To provide source/abi to Etherscan can run `brownie console`and then:

```bash
>> MobixToken.publish_source(mbx)
>> mbx = MobixToken.at(contract_address)
```

