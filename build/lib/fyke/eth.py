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
    method,
)


class EthRpc(BaseModel):
    def __init__(self):
        super().__init__()
        self._eth_tester = EthereumTester(backend=EELSBackend())

    @method(name="eth_getBlockByNumber")
    def get_block_by(self, block_identifier: BlockIdentifier, full_transactions: bool):
        if isinstance(block_identifier, str):
            return self._eth_tester.get_block_by_number(
                block_identifier, full_transactions=full_transactions
            )
        else:
            # TODO: assert is hash
            return self._eth_tester.get_block_by_hash(
                block_identifier, full_transactions=full_transactions
            )

    @method(name="eth_getBalance")
    def get_balance(self, acct: Address, block_identifier: BlockIdentifier):
        return self._eth_tester.get_balance(acct, block_number=block_identifier)

    @method(name="eth_getTransactionByHash")
    def get_transaction_by_hash(self, tx_hash: bytes):
        return self._eth_tester.get_transaction_by_hash(tx_hash)

    @method(name="eth_getTransactionReceipt")
    def get_transaction_receipt(self, tx_hash: bytes):
        return self._eth_tester.get_transaction_receipt(tx_hash)

    @method(name="eth_sendRawTransaction")
    def send_raw_transaction(self, raw_tx: bytes):
        return self._eth_tester.send_raw_transaction(raw_tx)
