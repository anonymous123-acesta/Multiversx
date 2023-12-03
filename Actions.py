from Librarii import *
from datetime import datetime, timedelta
import os

def delay(n):
    delay = timedelta(seconds=n)
    endtime = datetime.now() + delay
    while datetime.now() < endtime:
        pass

def semnare(t, signer, transC):
    t.signature = signer.sign(transC.compute_bytes_for_signing(t))
    return t

def output(t,proxy,hashes, number):
    transactions_dict = hashes[1]

    # Retrieve the transaction hash for key '0'
    transaction_hash = transactions_dict[number]

    information = proxy.get_transaction(transaction_hash)
    print(t.__dict__)
    print(information.nonce)
    print(information.status)
    delay = timedelta(seconds=1)
    endtime = datetime.now() + delay
    while datetime.now() < endtime:
        pass

def report_file(transaction,hashes,number,proxy):
    transactions_dict = hashes[1]
    transaction_hash = transactions_dict[number]
    information = proxy.get_transaction(transaction_hash)

    file_path = locatie
    t = str(transaction.__dict__)
    s = str(information.status)
    with open(file_path, "a") as f:
        f.write(t)
        f.write("\n")
        f.write(s)
        f.write("\n")
        f.write(" \n")