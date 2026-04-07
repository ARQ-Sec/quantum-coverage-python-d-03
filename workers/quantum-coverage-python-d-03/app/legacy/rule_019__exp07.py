from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

def execute():
    # rule_key: quantum.arq-q-0309-python
    ChaCha20Poly1305.generate_key()

if __name__ == '__main__':
    execute()
