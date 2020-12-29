# Block chain

# basic structure for bitcoints - Blockchain is a datastructure that verifies the integrity of a "transaction" using
# math. This ensures that the ledger cannot be manipulated and is proven mathematically which makes it such a good
# currency.

# You have a Blockchain
# Blockchain consists of blocks
# Each block is connect through hashing
# Each block has a unique digital fingerprint - transaction + previous block fingerprint
# Fingerprint change ealier in the chain effects all forward block fingerprints.


import hashlib
from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Ivan",
                                                     "Maria sent 1 BTC to Jenni",
                                                     "Satoshi sent 5 BTC to Hal Finney"])
second_block = Block(genesis_block.blockHash, ["Ivan sent 5 BTC to Liz",
                                               "John sent 5 BTC to Jenny"])
third_block = Block(second_block.blockHash, ["Amy sent 5 BTC to Benny",
                                             "Cody sent 1 BTC to Dan"])


print("Block hash: Genesis Block")
print(genesis_block.blockHash)
print("Block hash: Second Block")
print(second_block.blockHash)
print("Block hash: Third Block")
print(third_block.blockHash)



# Chaning the message changes the hash
# Change something in first block changes something in second block

