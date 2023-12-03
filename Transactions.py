from config import *
from multiversx_sdk_core import Transaction, Address
from multiversx_sdk_core import Token, TokenTransfer, TokenComputer
from multiversx_sdk_core.transaction_factories import TransferTransactionsFactory, TransactionsFactoryConfig, SmartContractTransactionsFactory

def transaction_true(account):
    t = Transaction(
        sender=adresa,
        receiver=adresa,
        chain_id="T",
        gas_limit=50000,
        amount=1000000000000000000,
        nonce=account.nonce
    )
    return t
    
def transaction_false_amount(account):
    t = Transaction(
        sender=adresa,
        receiver=adresa,
        chain_id="T",
        gas_limit=50000,
        amount=999999000000000000000000,
        nonce=account.nonce
    )
    return t

def transaction2_true(account):
    t = Transaction(
        sender=adresa,
        receiver=adresa,
        chain_id="T",
        gas_limit=50000,
        amount=1000000000000000000,
        nonce=account.nonce
    )
    return t

def transaction_EGDT_true():
    config = TransactionsFactoryConfig(chain_id="T")
    token = Token("A2B4-01d0d9")
    transfer = TokenTransfer(token, 1)
    transfer_factory = TransferTransactionsFactory(config, TokenComputer())

    alice = Address.new_from_bech32("erd15vdcwgq6n9934q487dnsn85ygke44j3lavk2udmjxmp2fe6dffzs69wp54")

    transaction = transfer_factory.create_transaction_for_esdt_token_transfer(
        sender=alice,
        receiver=alice,
        token_transfers=[transfer]
    )

    return transaction

def transaction_EGDT_false():
    config = TransactionsFactoryConfig(chain_id="T")
    token = Token("A2B4-01d0d9")
    transfer = TokenTransfer(token, 10)
    transfer_factory = TransferTransactionsFactory(config, TokenComputer())

    alice = Address.new_from_bech32("erd15vdcwgq6n9934q487dnsn85ygke44j3lavk2udmjxmp2fe6dffzs69wp54")

    transaction = transfer_factory.create_transaction_for_esdt_token_transfer(
        sender=alice,
        receiver=alice,
        token_transfers=[transfer]
    )

    return transaction

def transaction_smart_contract():
    config = TransactionsFactoryConfig(chain_id="T")
    sc_factory = SmartContractTransactionsFactory(config, TokenComputer())
    contract_address = Address.from_bech32("erd1qqqqqqqqqqqqqpgquzmh78klkqwt0p4rjys0qtp3la07gz4d396qn50nnm")

    alice = Address.new_from_bech32("erd15vdcwgq6n9934q487dnsn85ygke44j3lavk2udmjxmp2fe6dffzs69wp54")

    transaction = sc_factory.create_transaction_for_execute(
        sender=alice,
        contract=contract_address,
        function="foo",
        gas_limit=10000000,
        arguments=[42, "test"]
    )

    return transaction

