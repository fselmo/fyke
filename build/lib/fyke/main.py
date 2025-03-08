from jsonrpcserver import serve
from fyke.eth import EthRpc  # noqa: F401

if __name__ == "__main__":
    serve(name="fyke", port=5001)
