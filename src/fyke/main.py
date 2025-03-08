from pydantic import BaseModel

from eth_tester import (
    EELSBackend,
    EthereumTester,
)
from eth_typing import (
    Address,
    BlockIdentifier,
)
from jsonrpcserver import (
    Success,
    method,
    serve,
)


eth_tester = EthereumTester(backend=EELSBackend())


@method(name="eth_chainId")
def chain_id():
    return Success(eth_tester.chain_id())


@method(name="eth_accounts")
def accounts():
    return Success(eth_tester.get_accounts())


@method(name="eth_getBlockByNumber")
def get_block_by(block_identifier: BlockIdentifier, full_transactions: bool):
    if isinstance(block_identifier, str):
        return Success(eth_tester.get_block_by_number(
            block_identifier, full_transactions=full_transactions
        ))
    else:
        # TODO: assert is hash
        return Success(eth_tester.get_block_by_hash(
            block_identifier, full_transactions=full_transactions
        ))


@method(name="eth_getBalance")
def get_balance(acct: Address, block_identifier: BlockIdentifier):
    return Success(eth_tester.get_balance(acct, block_number=block_identifier))


@method(name="eth_getTransactionCount")
def get_transaction_count(acct: Address, block_identifier: BlockIdentifier):
    return Success(eth_tester.get_nonce(acct, block_identifier))


@method(name="eth_getTransactionByHash")
def get_transaction_by_hash(tx_hash: bytes):
    return Success(eth_tester.get_transaction_by_hash(tx_hash))


@method(name="eth_getTransactionReceipt")
def get_transaction_receipt(tx_hash: bytes):
    receipt = eth_tester.get_transaction_receipt(tx_hash)
    if receipt:
        # TODO: state_root in eth-tester serializer is Bytes32 which is not
        #  json serializable
        receipt["state_root"] = f"0x{receipt['state_root'].hex()}"
    return Success(receipt)


@method(name="eth_sendTransaction")
def send_transaction(tx: dict):
    return Success(eth_tester.send_transaction(tx))


@method(name="eth_sendRawTransaction")
def send_raw_transaction(raw_tx: bytes):
    return Success(eth_tester.send_raw_transaction(raw_tx))


@method(name="eth_estimateGas")
def estimate_gas(tx, block_identifier: BlockIdentifier):
    return Success(eth_tester.estimate_gas(tx, "latest"))


@method(name="eth_call")
def call(tx, block_identifier: BlockIdentifier):
    return Success(eth_tester.call(tx, block_identifier))


if __name__ == "__main__":
    serve(port=5001)
