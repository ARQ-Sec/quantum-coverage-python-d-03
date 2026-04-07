import hashlib

def execute():
    # rule_key: quantum.arq-q-0331-python
    hashlib.sha3_384(b"legacy").hexdigest()

if __name__ == '__main__':
    execute()
