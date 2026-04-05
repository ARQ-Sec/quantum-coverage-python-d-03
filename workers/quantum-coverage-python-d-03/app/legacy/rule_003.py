import hashlib

def execute():
    # rule_key: quantum.arq-q-0331-python
    hashlib.sha3_256(b"legacy").hexdigest()
    hashlib.sha3_512(b"legacy").hexdigest()

if __name__ == '__main__':
    execute()
