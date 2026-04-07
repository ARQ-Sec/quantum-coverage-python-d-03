from cryptography.hazmat.primitives.asymmetric import ec

def execute():
    # rule_key: quantum.arq-q-0314-python
    curve256 = ec.SECP256R1()
    curve384 = ec.SECP384R1()
    ec.generate_private_key(curve256)
    ec.generate_private_key(curve384)

if __name__ == '__main__':
    execute()
