from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305

def execute():
    # rule_key: quantum.arq-q-0333-python
    AESGCM.generate_key(bit_length=128)
    ChaCha20Poly1305.generate_key()

if __name__ == '__main__':
    execute()
