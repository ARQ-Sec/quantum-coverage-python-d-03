import jwt

def execute():
    # rule_key: quantum.arq-q-0320-python
    jwt.encode({"sub": "coverage"}, "secret", algorithm="RS256")
    jwt.encode({"sub": "coverage"}, "secret", algorithm="ES256")

if __name__ == '__main__':
    execute()
