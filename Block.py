import hashlib


class Block:
    def __init__(self, pHash, transaction):
        self.pHash = pHash
        self.transaction = transaction
        string_to_hash = "".join(transaction) + pHash
        self.blockHash = hashlib.sha256(string_to_hash.encode()).hexdigest()
