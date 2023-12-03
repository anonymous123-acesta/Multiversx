# Challenge for Multiversx

# Cerinta challenge
  Using python, the provided python sdk libraries (see below), and the above MultiversX transaction execution engine specifications/constraints, try to write some scenarios that interact with the devnet (or testnet) and verify (or not) the expectations for successfully executed transactions (e.g. eGLD transfer from one account to another - success or failed, smart contract call - success or failed etc.)
  The result of the test suite should generate a report with transaction execution statistics (e.g. total number of transactions, number of transactions successful, number of transactions failed, etc). 

# Pasi preliminari:
  - Instalare VM folosind Linux
  - Instalare tool-uri necesare realizarii proiectului (PyCharm, Postman)
  - Creare wallet pe Testnet (https://testnet-wallet.multiversx.com/dashboard)
  - Request Faucet din Wallet si realizarea unui numar de tranzactii direct de pe site
  - Interogarea tranzactiilor realizate folosing proxy in Postman (https://testnet-gateway.multiversx.com/transaction/HashTranzactie
  - Instalarea packetelor multiversx (core, wallet,network-provider) in terminal
# Realizarea proiectului in PyCharm:
  - Parcurgerea documentatiei (Cookbook) si familiarizarea cu functiile din cadrul pachetelor multiverx
  - Creearea mai multor fisiere pentru a decentraliza codul:
         * config.py = contine adrese, path-uri si parole stocate in variabile pentru o utilizare mai usoara in cod
         * Librarii.py = contine toate librariile utilizate in cod pentru a reduce liniile utilizate in restul fisierelor .py
         * Actions.py
         * Transactions.py
         * main.py
         * requirements.txt
         * raport.txt

  1) **config.py**
          Acest fisier contine adrese, path-uri si parole stocate ca si variabile globale pentru a putea fi utilizate cu mai multa usurinta in cod
  2) Librarii.py
            

