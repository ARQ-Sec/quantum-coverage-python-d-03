from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def execute():
    # rule_key: quantum.arq-q-0308-python
    AESGCM.generate_key(bit_length=128)

if __name__ == '__main__':
    execute()
