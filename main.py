from Librarii import *
def main():

    address = Address.new_from_bech32(adresa)
    proxy = ProxyNetworkProvider(testnet)
    secret_key = UserWallet.load_secret_key(Path(json_path), password, address_index=0)
    account = proxy.get_account(address)
    nonce_holder = AccountNonceHolder(account.nonce)
    signer = UserSigner.from_wallet(Path(json_path), password)
    transc = TransactionComputer()

    t = transaction_true(account)
    t1 = transaction_false_amount(account)
    t2 = transaction_pending(account)
    t3 = transaction2_true(account)
    t4 = transaction_EGDT_true()
    t5 = transaction_EGDT_false()
    t6 = transaction_smart_contract()

    t.nonce = nonce_holder.get_nonce_then_increment()
    t1.nonce = nonce_holder.get_nonce_then_increment()
    t2.nonce = nonce_holder.get_nonce_then_increment()
    t3.nonce = nonce_holder.get_nonce_then_increment()
    t4.nonce = nonce_holder.get_nonce_then_increment()
    t5.nonce = nonce_holder.get_nonce_then_increment()
    t6.nonce = nonce_holder.get_nonce_then_increment()

    tx = semnare(t, signer, transc, proxy)
    tx1 = semnare(t1, signer, transc, proxy)
    tx2 = semnare(t2, signer, transc, proxy)
    tx3 = semnare(t3, signer, transc, proxy)
    tx4 = semnare(t4, signer, transc, proxy)
    tx5 = semnare(t5, signer, transc, proxy)
    tx6 = semnare(t6, signer, transc, proxy)

    hashes = proxy.send_transactions([t, t1, t2, t3, t4, t5, t6])
    print("Transactions hashes:", hashes)

    delay(8)

    output(t, proxy, hashes, '0')
    output(t1, proxy, hashes, '1')
    output(t2, proxy, hashes, '2')
    output(t3, proxy, hashes, '3')
    output(t4, proxy, hashes, '4')
    output(t5, proxy, hashes, '5')
    output(t6, proxy, hashes, '6')

    report_file(t, hashes, '0', proxy)
    report_file(t1, hashes, '1', proxy)
    report_file(t2, hashes, '2', proxy)
    report_file(t3, hashes, '3', proxy)
    report_file(t4, hashes, '4', proxy)
    report_file(t5, hashes, '5', proxy)
    report_file(t6, hashes, '6', proxy)

if __name__ == '__main__':
    main()