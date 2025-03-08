# Fyke Net

Fyke Net is a Python library for interacting with the Ethereum Execution Layer Specifications (EELS) via JSON-RPC. 
It's a simple server that can be used to run tests against the EELS reference implementation.


# Run

Uses ``jsonrpcserver`` to run a JSON-RPC server. The server is started with the ``--port`` option, which specifies 
the port on which the server will listen for incoming requests. The default port is `5001`.

```bash
uv run python -m fyke.main
```

# Using with web3.py

```python
from web3 import Web3, HTTPProvider
from web3.providers.eth_tester.middleware import (
    ethereum_tester_middleware,
    default_transaction_fields_middleware,
)

w3 = Web3(
    HTTPProvider("http://127.0.1:5001"),
    middleware=[
        default_transaction_fields_middleware,
        ethereum_tester_middleware,
    ],
)

tx_hash = w3.eth.send_transaction({
    "from": w3.eth.accounts[0],
    "to": w3.eth.accounts[1],
    "value": 1234,
})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

latest = w3.eth.get_block("latest")

...
```
