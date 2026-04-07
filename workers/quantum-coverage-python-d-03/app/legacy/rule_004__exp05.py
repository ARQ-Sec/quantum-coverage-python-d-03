import hashlib

def execute():
    # rule_key: quantum.arq-q-0354-python
    hashlib.sha3_256(b"legacy").hexdigest()
    hashlib.shake_256(b"legacy").hexdigest(16)
    hashlib.blake2b(b"legacy").hexdigest()

if __name__ == '__main__':
    execute()
