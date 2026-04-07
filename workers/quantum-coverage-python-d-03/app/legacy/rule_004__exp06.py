import hashlib

def execute():
    # rule_key: quantum.arq-q-0332-python
    hashlib.blake2b(b"legacy").hexdigest()

if __name__ == '__main__':
    execute()
