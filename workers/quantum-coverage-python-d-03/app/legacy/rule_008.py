import jwt

def execute():
    # rule_key: quantum.arq-q-0339-python
    jwt.encode({"sub": "coverage"}, "secret", algorithm="RS256")

if __name__ == '__main__':
    execute()
