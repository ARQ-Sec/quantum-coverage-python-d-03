from cryptography.hazmat.primitives.asymmetric import rsa, ec

def execute():
    # rule_key: quantum.arq-q-0334-python
    rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ec.generate_private_key(ec.SECP256R1())

if __name__ == '__main__':
    execute()
